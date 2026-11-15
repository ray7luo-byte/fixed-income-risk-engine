from fire.data import fetch_treasury_curve
from fire.curve import bootstrap_zero_curve

par = fetch_treasury_curve()
zero = bootstrap_zero_curve(par)

print(f"{'tenor':>6} {'par':>8} {'zero':>8} {'diff(bp)':>9}")
for t in par.tenors:
    if t < 0.5:
        continue                       # 1mo/3mo 不在半年格点上，跳过
    p = par.rate(t)
    z = zero.rate(t)
    print(f"{t:>6} {p*100:>8.3f} {z*100:>8.3f} {(z-p)*1e4:>9.1f}")

import matplotlib.pyplot as plt
ts = zero.tenors
plt.plot(ts, [par.rate(t) * 100 for t in ts], label="par")
plt.plot(ts, [z * 100 for z in zero.rates], label="zero")
plt.xlabel("tenor (years)"); plt.ylabel("%"); plt.legend()
plt.savefig("docs/bootstrap.png")