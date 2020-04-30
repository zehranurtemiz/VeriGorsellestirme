import pandas as pd
ogrenci = pd.read_csv("ogrenci.csv")

print(ogrenci.sort_values(by="BOY",ascending=False).head())
