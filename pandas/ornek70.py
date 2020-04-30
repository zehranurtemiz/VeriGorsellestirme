import pandas as pd
yas_pd_series = pd.Series({"A":33,"B":24,"C":45,"E":18},name="yaş")
kilo_pd_series = pd.Series({"A":55,"B":65,"C":75,"D":80},name="kilo")
print(pd.DataFrame({"yaş":yas_pd_series,"kilo":kilo_pd_series}))

