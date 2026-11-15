from fire.curve import Curve
from fire.curve import Curve, bootstrap_zero_curve
from fire.pricing import bond_price_from_curve

def test_rate_interpolation():
    c = Curve([1, 2, 3, 5], [0.04, 0.045, 0.05, 0.055])
    assert abs(c.rate(2.5) - 0.0475) < 1e-12
    assert abs(c.rate(4) - 0.0525) < 1e-12
    assert abs(c.rate(2) - 0.045) < 1e-12       # 正好在点上
    assert abs(c.rate(0.5) - 0.04) < 1e-12      # 左端平推
    assert abs(c.rate(10) - 0.055) < 1e-12      # 右端平推

def test_df_matches_pricing():
    from fire.pricing import discount_factor
    c = Curve([1, 2], [0.04, 0.05])
    assert abs(c.df(1.5) - discount_factor(0.045, 1.5, "semi")) < 1e-12

def test_bootstrap_values():
    par = Curve([0.5, 1.0, 1.5], [0.04, 0.05, 0.06])
    z = bootstrap_zero_curve(par, max_years=1.5)
    assert z.tenors == [0.5, 1.0, 1.5]
    assert abs(z.rates[0] - 0.04) < 1e-12          # 第一个点 zero = par
    assert abs(z.rates[1] - 0.050125624) < 1e-9
    assert abs(z.rates[2] - 0.060407097) < 1e-9

def test_bootstrap_reprices_par_bonds_at_100():
    par = Curve([0.5, 1.0, 1.5], [0.04, 0.05, 0.06])
    z = bootstrap_zero_curve(par, max_years=1.5)
    assert abs(bond_price_from_curve(100, 0.05, 1.0, z) - 100) < 1e-9
    assert abs(bond_price_from_curve(100, 0.06, 1.5, z) - 100) < 1e-9