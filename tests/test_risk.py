from fire.pricing import price_from_ytm
from fire.risk import dv01, modified_duration, convexity

FACE, CPN, YRS, Y = 100, 0.05, 2, 0.05

def test_known_values():
    assert abs(dv01(FACE, CPN, YRS, Y) - 0.01881) < 1e-5
    assert abs(modified_duration(FACE, CPN, YRS, Y) - 1.8810) < 1e-4
    assert abs(convexity(FACE, CPN, YRS, Y) - 4.531) < 1e-3

def test_dv01_equals_duration_times_price():
    p = price_from_ytm(FACE, CPN, YRS, Y)
    assert abs(dv01(FACE, CPN, YRS, Y) - modified_duration(FACE, CPN, YRS, Y) * p * 0.0001) < 1e-8

def test_taylor_estimate():
    p = price_from_ytm(FACE, CPN, YRS, Y)
    D = modified_duration(FACE, CPN, YRS, Y)
    C = convexity(FACE, CPN, YRS, Y)
    dy = 0.01
    real = price_from_ytm(FACE, CPN, YRS, Y + dy) - p
    est = (-D * dy + 0.5 * C * dy ** 2) * p
    assert abs(real - est) < 1e-3

def test_zero_coupon_duration_near_maturity():
    assert abs(modified_duration(100, 0.0, 2, 0.05) - 1.951) < 1e-3