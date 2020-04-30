import pandas as pd
a_pd_series = pd.Series([1,2,3,4,5,6,7,8,9,10])
b_pd_series = pd.Series([1,2,3,4,5],index=["bir","iki","üç","dört","beş"])

print(a_pd_series[3])

print(b_pd_series["iki"])
