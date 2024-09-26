# Main file
# Auteur : Philippe Arsenault
# Fonction solo qui prend une array de data et qui fait une image
from txt2data import txt2data
from make_image import make_image
import matplotlib.pyplot as plt


data = []
axe_x = [1540,1560,'Longueur d\'onde (nm)']
axe_y = [-70,10,'Puissance (dB)']

# Diode DFB - 10 Degrés
plt.figure(1)
for i in range(9):
    path = "Labo1/images Labo 1/DFB/DFB_10deg_"+str(5*i)+"ma.txt"
    #data["data{0}".format(5*i)] = txt2data(path)
    data = txt2data(path)
    make_image(data,title='DFB 10C',axe_x=axe_x,axe_y=axe_y,label = str(5*i)+'mA')


# Diode DFB - 20 Degrés
plt.figure(2)
for i in range(9):
    path = "Labo1/images Labo 1/DFB/DFB_20deg_"+str(5*i)+"ma.txt"
    #data["data{0}".format(5*i)] = txt2data(path)
    data = txt2data(path)
    make_image(data,title='DFB 20C',axe_x=axe_x,axe_y=axe_y,label = str(5*i)+'mA')


axe_x = [1460,1610,'Longueur d\'onde (nm)']
axe_y = [-70,-20,'Puissance (dB)']

# Diode SLED - 10 Degrés
plt.figure(3)
for i in range(7):
    path = "Labo1/images Labo 1/SLED/SLED_10deg_"+str(20*i)+"ma.txt"
    #data["data{0}".format(5*i)] = txt2data(path)
    data = txt2data(path)
    make_image(data,title='SLED 10C',axe_x=axe_x,axe_y=axe_y,label = str(20*i)+'mA')


# Diode SLED - 20 Degrés
plt.figure(4)
for i in range(7):
    path = "Labo1/images Labo 1/SLED/SLED_20deg_"+str(20*i)+"ma.txt"
    #data["data{0}".format(5*i)] = txt2data(path)
    data = txt2data(path)
    make_image(data,title='SLED 20C',axe_x=axe_x,axe_y=axe_y,label = str(20*i)+'mA')
plt.show()



""" # Diode DFB - 10 Degrés
for i in range(9):
    path = "Labo1/images Labo 1/DFB/DFB_10deg_"+str(5*i)+"ma.txt"
    #data["data{0}".format(5*i)] = txt2data(path)
    data = txt2data(path)
    make_image(data,title='DFB 10C',axe_x=axe_x,axe_y=axe_y,label = str(5*i)+'mA')
plt.show() """


