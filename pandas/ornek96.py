import pandas as pd
ogrenci = pd.read_csv("ogrenci.csv")

print(ogrenci.drop(range(2,ogrenci.shape[0])))
