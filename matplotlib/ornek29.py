import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
x=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
x2=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
y2=[4,5,8,14,19,23,24,25,23,15,11,6]
plt.scatter(x,y,label="2019",s=75,c="#6baed6",edgecolors='black')
plt.scatter(x2,y2,label="2018",s=50,c="#2171b5",edgecolors='black')
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")
plt.legend()
plt.show()
