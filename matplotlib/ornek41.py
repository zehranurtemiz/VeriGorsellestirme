import matplotlib.pyplot as plt

plt.subplots(figsize=(14,7))

labels = ('Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık')
sizes = [3,4,7,12,17,21,24,24,21,15,9,4]
colors = ['#ff6666','#468499','#ff7f50','#ffdab9','#00ced1', '#ffff66','#088da5','#daa520','#794044','#a0db8e','#b4eeb4','#c0d6e4','#065535','#d3ffce']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',pctdistance=0.7);
plt.show()
