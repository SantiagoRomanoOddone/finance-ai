import sys, glob, yaml

MONTHS_DIR = "months"

def latest_config():
    files = sorted(glob.glob(f"{MONTHS_DIR}/*.yaml"))
    if not files:
        raise SystemExit(f"No configs in {MONTHS_DIR}/")
    return files[-1]

def main(amount, cfg_path=None):
    cfg_path = cfg_path or latest_config()
    print(f"Using config: {cfg_path}")
    cfg = yaml.safe_load(open(cfg_path))
    alloc = cfg["allocation"]
    breakdown = cfg.get("breakdown", {})

    s = sum(alloc.values())
    if abs(s - 1.0) > 1e-6:
        print(f"WARN: allocation sums to {s:.4f}, not 1.0")

    print(f"\n=== Main allocation (${amount:,.2f}) ===")
    print(f"{'Asset':<10} {'USD':>10}")
    for name, w in alloc.items():
        print(f"{name:<10} {amount*w:>10.2f}")
    print(f"{'TOTAL':<10} {amount:>10.2f}")

    for group, sub in breakdown.items():
        sub_s = sum(sub.values())
        if sub_s > 0 and abs(sub_s - 1.0) > 1e-6:
            print(f"\nWARN: breakdown '{group}' sums to {sub_s:.4f}, not 1.0")
        group_amt = amount * alloc.get(group, 0)
        print(f"\n=== {group} breakdown (${group_amt:,.2f}) ===")
        print(f"{'Ticker':<10} {'USD':>10}")
        for t, sw in sub.items():
            v = group_amt * sw
            if v > 0:
                print(f"{t:<10} {v:>10.2f}")
        print(f"{'TOTAL':<10} {group_amt:>10.2f}")

if __name__ == "__main__":
    amount = float(sys.argv[1])
    cfg = sys.argv[2] if len(sys.argv) > 2 else None
    main(amount, cfg)
