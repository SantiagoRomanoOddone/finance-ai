import sys, glob, yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
MONTHS_DIR = ROOT / "months"

def latest_config():
    files = sorted(MONTHS_DIR.glob("*.yaml"))
    if not files:
        raise SystemExit(f"No configs in {MONTHS_DIR}/")
    return files[-1]

def main(amount, cfg_path=None):
    cfg_path = Path(cfg_path) if cfg_path else latest_config()
    print(f"Using config: {cfg_path.relative_to(ROOT)}")
    cfg = yaml.safe_load(cfg_path.open())
    alloc = cfg["allocation"]
    breakdown = cfg.get("breakdown", {})

    s = sum(alloc.values())
    if abs(s - 1.0) > 1e-6:
        print(f"WARN: allocation sums to {s:.4f}, not 1.0")

    print(f"\n=== Main allocation (${amount:,.0f}) ===")
    print(f"{'Asset':<10} {'USD':>10}")
    for name, w in alloc.items():
        print(f"{name:<10} {round(amount*w):>10}")
    print(f"{'TOTAL':<10} {round(amount):>10}")

    for group, sub in breakdown.items():
        sub_s = sum(sub.values())
        if sub_s > 0 and abs(sub_s - 1.0) > 1e-6:
            print(f"\nWARN: breakdown '{group}' sums to {sub_s:.4f}, not 1.0")
        group_amt = amount * alloc.get(group, 0)
        print(f"\n=== {group} breakdown (${group_amt:,.0f}) ===")
        print(f"{'Ticker':<10} {'USD':>10}")
        for t, sw in sub.items():
            v = group_amt * sw
            if v > 0:
                print(f"{t:<10} {round(v):>10}")
        print(f"{'TOTAL':<10} {round(group_amt):>10}")

if __name__ == "__main__":
    amount = float(sys.argv[1])
    cfg = sys.argv[2] if len(sys.argv) > 2 else None
    main(amount, cfg)
