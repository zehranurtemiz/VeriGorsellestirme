import matplotlib.pyplot as plt#Matplotlib kütüphanesi aktif edilir.

plt.figure(figsize=(10,4))#Grafiğin boyutunu belirler. 
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran",
   "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,13,17,21,24,24,21,15,9,4]

plt.plot(x,y)#Grafiğin ana komutunu oluşturur.
plt.xlabel("AY")#x ekseninin başlığını oluşturur.
plt.ylabel("DERECE")#y ekseninin başlığını oluşturur.
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")#Grafiğin başlığını oluşturur.

plt.show()#Grafiği çizdirmemizi sağlar.
