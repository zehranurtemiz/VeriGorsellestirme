import matplotlib.pyplot as plt
plt.figure(figsize=(16,4))

plt.subplot(1,2,1)
x=["Ock","Şbt","Mrt","Nsn","Mys","Hzrn","Tmmz","Ağsts","Eyll","Ekm","Ksm","Arlk"]
y2=[4,5,8,14,19,23,24,25,23,15,11,6]
plt.plot(x,y2,color="red")
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2018 YILI ORTALAMA SICAKLIK ANALİZİ")

plt.subplot(1,2,2)   
x=["Ock","Şbt","Mrt","Nsn","Mys","Hzrn","Tmmz","Ağsts","Eyll","Ekm","Ksm","Arlk"]
y=[3,4,7,12,17,21,24,24,21,15,9,4]
plt.plot(x,y,color="black")
plt.xlabel("AY")
plt.ylabel("DERECE")
plt.title("2019 YILI ORTALAMA SICAKLIK ANALİZİ")

plt.show()
