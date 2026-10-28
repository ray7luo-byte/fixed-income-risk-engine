from fire.pricing import discount_factor, zero_rate, bond_price, shift_curve,price_from_ytm,ytm_from_price

def test_discount_factor_annual():
    assert abs(discount_factor(0.05, 2, "annual") - 0.907029) < 1e-6

def test_zero_rate_roundtrip():
    d = discount_factor(0.0494, 2, "semi")
    assert abs(zero_rate(d, 2, "semi") - 0.0494) < 1e-9

def test_bond_price_par():
    # 票息等于利率 → 价格等于面值
    assert abs(bond_price(100, 0.05, 2, [0.05]*4) - 100.0) < 1e-6

def test_bond_price_known():
    assert abs(bond_price(100, 0.05, 2, [0.040, 0.042, 0.045, 0.048]) - 100.411) < 1e-3

def test_shift_curve():
    out = shift_curve([0.04, 0.05], 0.0001)
    assert all(abs(a - b) < 1e-12 for a, b in zip(out, [0.0401, 0.0501]))

def test_price_from_ytm_par():
    assert abs(price_from_ytm(100, 0.05, 2, 0.05) - 100.0) < 1e-6

def test_price_from_ytm_known():
    assert abs(price_from_ytm(100, 0.05, 2, 0.06) - 98.141) < 1e-3
    assert abs(price_from_ytm(100, 0.05, 2, 0.04) - 101.904) < 1e-3

def test_ytm_roundtrip():
    # 算出的 y 代回去，价格要还原
    p = 100.411
    y = ytm_from_price(100, 0.05, 2, p)
    assert abs(price_from_ytm(100, 0.05, 2, y) - p) < 1e-6

def test_ytm_par():
    # 平价债的 YTM 等于票息率
    assert abs(ytm_from_price(100, 0.05, 2, 100.0) - 0.05) < 1e-8