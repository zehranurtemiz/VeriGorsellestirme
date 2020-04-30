import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.step(x,y,marker="o",c="#2171b5",where='mid',linewidth=3)
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.show()
