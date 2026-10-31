from fire.curve import Curve

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