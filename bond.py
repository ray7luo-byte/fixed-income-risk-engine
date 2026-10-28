import math

def discounted_factor(r,t,conv):
    if conv=='annual':
        return (1+r)**(-t)
    elif conv=='semi':
        return (1+r/2)**(-2*t)
    elif conv=='cont':
        return math.exp(-r*t)

def zero_rate(d,t,conv):
    if conv=="annual":
        return d**(-1/t)-1
    elif conv=='semi':
        return 2*(d**(-1/(2*t))-1)
    elif conv=='cont':
        return -math.log(d)/t

#print(zero_rate(0.9070,2,"annual"))
#print(zero_rate(0.9070,2,"semi"))
#print(zero_rate(0.9070,2,"cont"))


def bond_price(face, coupon_rate,years,zero_rates):
    price =0
    cashflow_semi=face*coupon_rate/2
    for i in range(1,2*years+1):
        price=price+cashflow_semi*discounted_factor(zero_rates[i-1], i/2, "semi")
    price=price+face*discounted_factor(zero_rates[-1], years, "semi")
    return price
curve = [0.040, 0.042, 0.045, 0.048]
print(bond_price(100, 0.05, 2, curve))


def shift_curve(zero_rates, bump):
    return[r+bump for r in zero_rates]
base = [0.040, 0.042, 0.045, 0.048]
p_up1=bond_price(100,0.05,2,shift_curve(base,0.0001))
p_dn1=bond_price(100,0.05,2,shift_curve(base,-0.0001))
p_up100=bond_price(100,0.05,2,shift_curve(base,0.01))
p_dn100=bond_price(100,0.05,2,shift_curve(base,-0.01))
p0=bond_price(100,0.05,2,base)

DV01=p0-p_up1

print(DV01, p_up1,p_up100,p_dn100)
