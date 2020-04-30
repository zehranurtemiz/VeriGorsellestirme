import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.plot(x,y,color="red",linewidth=1,linestyle="-",marker="o",
         markersize=10,label="sıcaklık",alpha=0.9)
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.text(x=4,y=22,s="Yılın en sıcak ayı olmuştur.",backgroundcolor="green",
         fontdict={"color":"white","fontsize":10})
plt.legend()
plt.show()
