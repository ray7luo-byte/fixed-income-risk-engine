import pandas as pd

# FRED 代码 → 期限（年）
FRED_SERIES = {
    "DGS1MO": 1/12, "DGS3MO": 0.25, "DGS6MO": 0.5, "DGS1": 1, "DGS2": 2,
    "DGS3": 3, "DGS5": 5, "DGS7": 7, "DGS10": 10, "DGS20": 20, "DGS30": 30,
}

# 把 11 个代码用逗号连起来，拼进网址
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=" + ",".join(FRED_SERIES.keys())


def _row_to_curve(row):
    """FRED 的一行 → {期限(年): 收益率(小数)}，按期限排序。"""
    curve = {}
    for code, tenor in FRED_SERIES.items():
        if code in row:
            curve[tenor] = row[code] / 100      # FRED 给 4.25，我们要 0.0425
    return dict(sorted(curve.items()))


def fetch_treasury_curve():
    """从 FRED 拉最新一天完整的国债收益率曲线。"""
    df = pd.read_csv(FRED_URL, na_values=".")   # 读网上的 CSV，"." 当缺失
    row = df.dropna().iloc[-1]                  # 丢掉有缺失的行，取最后一行
    return _row_to_curve(row)