import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.bar(x,y,label="sıcaklık",width=0.7,color="#f9af2b",edgecolor="#f05131",)
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.legend()
plt.show()
