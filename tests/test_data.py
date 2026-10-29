import pandas as pd
from fire.data import _row_to_curve

def test_row_to_curve():
    row = pd.Series({"DGS1": 4.0, "DGS2": 4.2, "DGS10": 4.5})
    assert _row_to_curve(row) == {1: 0.040, 2: 0.042, 10: 0.045}