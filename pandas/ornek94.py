import pandas as pd
veri = pd.read_csv("veri.csv")
print(veri.iloc[1:3,0:2])
