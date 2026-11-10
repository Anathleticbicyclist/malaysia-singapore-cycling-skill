#!/usr/bin/env python3
"""KLIA 寄存费用测算：按件、按 24 小时、支持第二档单价与人均分摊。

示例：
    python storage_cost.py --items 3 --days 9 --rate 48
    python storage_cost.py --items 3 --days 10 --rate 48 --tier2 42 --tier2-from 7 --people 3
"""

import argparse


def compute(items, days, rate, tier2, tier2_from, people, fx):
    if tier2 is None:
        tier1_days, tier2_days = days, 0
    else:
        tier1_days = min(days, max(0, tier2_from - 1)) if tier2_from > 0 else days
        tier2_days = max(0, days - tier1_days)
    tier1_cost = items * tier1_days * rate
    tier2_cost = items * tier2_days * (tier2 if tier2 is not None else rate)
    total = tier1_cost + tier2_cost
    return {
        "items": items,
        "days": days,
        "tier1_days": tier1_days,
        "tier1_rate": rate,
        "tier1_cost": tier1_cost,
        "tier2_days": tier2_days,
        "tier2_rate": tier2 if tier2 is not None else rate,
        "tier2_cost": tier2_cost,
        "total_myr": total,
        "per_person_myr": total / people if people else total,
        "total_cny": total * fx,
        "per_person_cny": (total * fx / people) if people else total * fx,
    }


def main():
    p = argparse.ArgumentParser(description="KLIA 寄存费用测算")
    p.add_argument("--items", type=int, default=3, help="件数，默认 3")
    p.add_argument("--days", type=int, required=True, help="存放的 24 小时段数（必填）")
    p.add_argument("--rate", type=float, required=True, help="第一档单价 RM/件/24h（必填）")
    p.add_argument("--tier2", type=float, default=None, help="第二档单价 RM/件/24h")
    p.add_argument("--tier2-from", type=int, default=7, help="第二档从第几段开始，默认第 7 段")
    p.add_argument("--people", type=int, default=3, help="人数，用于人均分摊，默认 3")
    p.add_argument("--fx", type=float, default=1.7, help="1 MYR 折 CNY 汇率，默认 1.7（按当日为准）")
    args = p.parse_args()

    if args.items <= 0 or args.days <= 0 or args.rate <= 0:
        p.error("items / days / rate 必须为正数")

    r = compute(args.items, args.days, args.rate, args.tier2, args.tier2_from,
                args.people, args.fx)

    print("寄存费用测算")
    print(f"  件数：{r['items']}  存放：{r['days']} 个 24 小时段")
    print(f"  第一档：{r['tier1_days']} 天 × RM{r['tier1_rate']:g} = RM{r['tier1_cost']:,.2f}")
    if r["tier2_days"] > 0:
        print(f"  第二档：{r['tier2_days']} 天 × RM{r['tier2_rate']:g} = RM{r['tier2_cost']:,.2f}")
    print(f"  合计：RM{r['total_myr']:,.2f}  约 ¥{r['total_cny']:,.0f}（汇率 {args.fx:g}）")
    print(f"  人均：RM{r['per_person_myr']:,.2f}  约 ¥{r['per_person_cny']:,.0f}")
    print("注：汇率与旺季附加费以当日实际为准；超过 3 个月未取视为放弃。")


if __name__ == "__main__":
    main()
