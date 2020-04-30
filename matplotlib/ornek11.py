import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.plot(x,y,color="green",linewidth=2,linestyle="--",marker="o",markersize=12,markerfacecolor="yellow",markeredgewidth=5,markeredgecolor="blue")
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.show()
