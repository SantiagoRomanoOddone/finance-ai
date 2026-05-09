import sys, io, contextlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import invest

def latest_month():
    return sorted((ROOT / "months").glob("*.yaml"))[-1]

def main(amount):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        invest.main(amount)
    invest_output = buf.getvalue()

    month_path = latest_month()
    profile = (ROOT / "config" / "profile.yaml").read_text()
    month_cfg = month_path.read_text()
    prompt = (ROOT / "config" / "prompt.md").read_text()

    print("=" * 60)
    print(prompt)
    print("\n" + "=" * 60)
    print("## profile.yaml\n```yaml")
    print(profile.rstrip())
    print("```")
    print(f"\n## {month_path.relative_to(ROOT)}\n```yaml")
    print(month_cfg.rstrip())
    print("```")
    print(f"\n## Investment plan for ${amount:,.0f}\n```")
    print(invest_output.rstrip())
    print("```")

if __name__ == "__main__":
    main(float(sys.argv[1]))
