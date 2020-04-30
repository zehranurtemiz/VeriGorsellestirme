import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.plot(x,y)
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.savefig(fname="grafik3.png",
            #Grafiğin kaydedileceği dosya adı tanımlanır.
            facecolor="#f0f9e8",
            #Grafiğin arka planı rengi tanımlanır. 
            transparent=True)
            #Grafiğin iç kısmının rengi ile arka plan aynı olması için tanımlanır.
plt.show()
