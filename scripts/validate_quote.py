"""Compare model YTM/price against a live Treasury quote (WSJ Treasury Quotes)."""
from fire.pricing import ytm_from_price, price_from_ytm

# ---- 查询数 ----
coupon = 0.04625          
years = 2                 # 到期日减今天，四舍五入到 0.5 年
asked_price = 100.033     
asked_yield = 0.04569      
# --------------------------------

model_yield = ytm_from_price(100, coupon, years, asked_price)
model_price = price_from_ytm(100, coupon, years, asked_yield)

print(f"quote yield  {asked_yield*100:.3f}%   model yield  {model_yield*100:.3f}%   diff {(model_yield-asked_yield)*1e4:+.1f} bp")
print(f"quote price  {asked_price:.3f}    model price  {model_price:.3f}    diff {model_price-asked_price:+.3f}")