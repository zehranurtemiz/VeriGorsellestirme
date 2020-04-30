import pandas as pd
örnek = {"isim":["Gül","Onur","Emine","Yakup","Arzu","Naci"],
       "cinsiyet":["K","E","K","E","K","E"],
       "boy":[170,175,165,170,170,185],
       "kilo":[55,65,50,55,55,75],
       "yaş":[27,21,24,20,27,29]}
df_bilgiler = pd.DataFrame(örnek)
print(df_bilgiler.groupby("cinsiyet").sum())
