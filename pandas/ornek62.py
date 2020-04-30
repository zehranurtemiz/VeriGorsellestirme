import pandas as pd
a_pd_series = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a_pd_series[3:5]),
b_pd_series = pd.Series([1,2,3,4,5],index=["bir","iki","üç","dört","beş"])
print("\n")
print(b_pd_series["iki":"dört"])
