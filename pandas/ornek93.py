import pandas as pd
veri = pd.read_csv("veri.csv")
print(veri.loc[[1,2,3],["NEM","RUZGAR"]])
