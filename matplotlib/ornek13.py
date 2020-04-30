import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
y2=[4,5,8,14,19,23,24,25,23,15,11,6]
plt.plot(x,y,color="r",linewidth=3,linestyle="--",marker="o",markersize=12,markerfacecolor="yellow",markeredgewidth=5,markeredgecolor="blue",alpha=0.5)
plt.plot(x,y2,color="blue",linewidth=3,linestyle=":", marker="o", markerfacecolor="yellow",markeredgewidth=4, markeredgecolor="blue", alpha=0.9)
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2018 - 2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.show()
