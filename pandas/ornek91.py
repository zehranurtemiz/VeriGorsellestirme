import pandas as pd
veri = pd.read_csv("veri.csv")
print(veri[["SICAKLIK","NEM"]].head())
