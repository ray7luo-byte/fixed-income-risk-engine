"""Scratch experiments from week 1. Run from repo root: python -m scripts.experiments"""
from fire.pricing import zero_rate, bond_price, shift_curve

# Day 1: same discount factor, three conventions
print(zero_rate(0.9070, 2, "annual"), zero_rate(0.9070, 2, "semi"), zero_rate(0.9070, 2, "cont"))

# Day 2: price off a zero curve
base = [0.040, 0.042, 0.045, 0.048]
p0 = bond_price(100, 0.05, 2, base)
print("price", p0)

# Day 3: parallel shifts, DV01 and convexity
p_up1 = bond_price(100, 0.05, 2, shift_curve(base, 0.0001))
p_dn1 = bond_price(100, 0.05, 2, shift_curve(base, -0.0001))
p_up100 = bond_price(100, 0.05, 2, shift_curve(base, 0.01))
p_dn100 = bond_price(100, 0.05, 2, shift_curve(base, -0.01))
DV01 = p0 - p_up1
print("DV01", DV01, "up100", p_up100, "dn100", p_dn100)

from fire.data import fetch_treasury_curve
print(fetch_treasury_curve())