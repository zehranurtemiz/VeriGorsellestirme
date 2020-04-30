import pandas as pd
ogrenci = pd.read_csv("ogrenci.csv")

print(ogrenci.drop("CINSIYET",axis=1).head())
