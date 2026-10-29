from fire.pricing import price_from_ytm

def _bumped_prices(face,coupon_rate,years,y,h):
    p0=price_from_ytm(face,coupon_rate,years,y)
    price_up=price_from_ytm(face,coupon_rate,years,y+h)
    price_down=price_from_ytm(face,coupon_rate,years,y-h)
    return price_up,price_down,p0

def dv01(face,coupon_rate,years,y,h=0.0001):
    price_up, price_down,_ = _bumped_prices(face, coupon_rate, years, y, h)
    return (price_down-price_up)/2

def modified_duration(face,coupon_rate,years,y,h=0.0001):
    price_up, price_down,p0 = _bumped_prices(face, coupon_rate, years, y, h)
    return (price_down-price_up)/(2*p0*h)

def convexity(face,coupon_rate,years,y,h=0.0001):
    price_up, price_down,p0 = _bumped_prices(face, coupon_rate, years, y, h)
    return (price_up+price_down-2*p0)/(p0*h**2)