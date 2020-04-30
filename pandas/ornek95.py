import pandas as pd
ogrenci = pd.read_csv("ogrenci.csv")

print(ogrenci[ (ogrenci["YAS"]>18) & (ogrenci["YAS"]<25)])
