  # Fixed Income Risk Engine
  Bond pricing, yield curves and risk metrics (DV01, duration, convexity) in Python.
  ## Validation against a live Treasury quote

Quote source: WSJ Treasury Quotes, 2026-10-30. Bond: [10-31-2028], coupon [4.625]%, asked 100.033, asked yield 4.569%.

| | Quote | Model | Diff |
|---|---|---|---|
| Yield | 4.569% | 4.608% | +3.9 bp |
| Price | 100.033 | 100.106 | +0.073 |

The gap comes from three simplifications in the current model, all scheduled for the Bond class in week 2:
1. **Accrued interest** — the quote is a clean price; the model computes a dirty price.
2. **Non-integer periods** — maturity is rounded to whole half-years; the real bond has a fractional first period.
3. **Day count** — Treasuries use actual/actual; the model has no calendar.