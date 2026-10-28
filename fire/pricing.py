import math


def discount_factor(r, t, conv):
    """Discount factor d(t) for annual rate r, time t in years."""
    if conv == 'annual':
        return (1 + r) ** (-t)
    elif conv == 'semi':
        return (1 + r / 2) ** (-2 * t)
    elif conv == 'cont':
        return math.exp(-r * t)


def zero_rate(d, t, conv):
    """Inverse of discount_factor: rate implied by d(t)."""
    if conv == "annual":
        return d ** (-1 / t) - 1
    elif conv == 'semi':
        return 2 * (d ** (-1 / (2 * t)) - 1)
    elif conv == 'cont':
        return -math.log(d) / t


def bond_price(face, coupon_rate, years, zero_rates):
    """Price a semiannual-coupon bond off a list of zero rates (one per half-year)."""
    price = 0
    cashflow_semi = face * coupon_rate / 2
    for i in range(1, 2 * years + 1):
        price = price + cashflow_semi * discount_factor(zero_rates[i - 1], i / 2, "semi")
    price = price + face * discount_factor(zero_rates[-1], years, "semi")
    return price


def shift_curve(zero_rates, bump):
    """Parallel shift: add bump to every rate."""
    return [r + bump for r in zero_rates]
