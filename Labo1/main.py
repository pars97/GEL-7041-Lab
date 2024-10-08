# Main file
# Auteur : Philippe Arsenault
# Fonction solo qui prend une array de data et qui fait une image
from txt2data import txt2data
from make_image import make_image,new_color
from Integrale_numerique import numeric_integral as ni
import matplotlib.pyplot as plt
from LOC import LOC
from FWHM import FWHM
import scipy.signal as sig
from SLSR import SLSR


data_x = [] 
data_y = []


#Variable de sortie CHANGER ICI POUR QUE LE CODE SORTE QUELQUE CHOSE
image = False
puissance_totale = False
lambda_centre = True
fwhm_DFB = False
slsr = False
fsr = True


if image:    
    axe_x = [1540,1560,'Longueur d\'onde (nm)']
    axe_y = [-70,10,'Puissance (dBm)']
    plt.figure(1)
    for i in range(9):
        path = "Labo1/images Labo 1/DFB/DFB_10deg_"+str(5*i)+"ma.txt"
        data_x,data_y = txt2data(path)
        make_image(data_x,data_y,title='DFB 10C',axe_x=axe_x,axe_y=axe_y,label = str(5*i)+'mA',couleur=new_color(i))


    # Diode DFB - 20 Degrés
    plt.figure(2)
    for i in range(9):
        path = "Labo1/images Labo 1/DFB/DFB_20deg_"+str(5*i)+"ma.txt"
        data_x,data_y = txt2data(path)
        make_image(data_x,data_y,title='DFB 20C',axe_x=axe_x,axe_y=axe_y,label = str(5*i)+'mA',couleur=new_color(i))

    axe_x = [1460,1610,'Longueur d\'onde (nm)']
    axe_y = [-70,-20,'Puissance (dBm)']

    # Diode SLED - 10 Degrés
    plt.figure(3)
    for i in range(7):
        path = "Labo1/images Labo 1/SLED/SLED_10deg_"+str(20*i)+"ma.txt"
        data_x,data_y = txt2data(path)
        make_image(data_x,data_y,title='SLED 10C',axe_x=axe_x,axe_y=axe_y,label = str(20*i)+'mA',couleur=new_color(i))


    # Diode SLED - 20 Degrés
    plt.figure(4)
    for i in range(7):
        path = "Labo1/images Labo 1/SLED/SLED_20deg_"+str(20*i)+"ma.txt"
        data_x,data_y = txt2data(path)
        make_image(data_x,data_y ,title='SLED 20C',axe_x=axe_x,axe_y=axe_y,label = str(20*i)+'mA',couleur=new_color(i))
    
    plt.show()

if puissance_totale:

    # SLED 20C
    lin,db = ni(file_path="Labo1/images Labo 1/SLED/SLED_20deg_120ma.txt")
    print("La puissance totale de la SLED à 20C est de {lin} mW et de {db} dBm.".format(lin = round(lin,4),db=round(db,2)))

    # SLED 10C
    lin,db = ni(file_path="Labo1/images Labo 1/SLED/SLED_10deg_120ma.txt")
    print("La puissance totale de la SLED à 10C est de {lin} mW et de {db} dBm.".format(lin = round(lin,4),db=round(db,2)))

    # DFB 20C
    lin,db = ni(file_path="Labo1/images Labo 1/DFB/DFB_20deg_40ma.txt")
    print("La puissance totale de la DFB à 20C est de {lin} mW et de {db} dBm.".format(lin = round(lin,4),db=round(db,2)))

    # DFB 10C
    lin,db = ni(file_path="Labo1/images Labo 1/DFB/DFB_10deg_40ma.txt")
    print("La puissance totale de la DFB à 10C est de {lin} mW et de {db} dBm.".format(lin = round(lin,4),db=round(db,2))) 

if lambda_centre:
    loc,maxi,eV = LOC(file_path="Labo1/images Labo 1/SLED/SLED_20deg_120ma.txt")
    print("La longueur d'onde central de la SLED à 20C est de {loc} nm correspondant à {eV} eV, puissance de {maxi_lin} mW ({maxi_db}dBm)."
          .format(loc = round(loc,3),eV=round(eV,4),maxi_lin=round(maxi[0],4),maxi_db = round(maxi[1],2)))

    loc,maxi,eV = LOC(file_path="Labo1/images Labo 1/SLED/SLED_10deg_120ma.txt")
    print("La longueur d'onde central de la SLED à 10C est de {loc} nm correspondant à {eV} eV, puissance de {maxi_lin} mW ({maxi_db}dBm)."
          .format(loc = round(loc,3),eV=round(eV,4),maxi_lin=round(maxi[0],4),maxi_db = round(maxi[1],2)))

    loc,maxi,eV = LOC(file_path="Labo1/images Labo 1/DFB/DFB_20deg_40ma.txt")
    print("La longueur d'onde central de la DFB à 20C est de {loc} nm correspondant à {eV} eV, puissance de {maxi_lin} mW ({maxi_db}dBm)."
          .format(loc = round(loc,3),eV=round(eV,4),maxi_lin=round(maxi[0],4),maxi_db = round(maxi[1],2)))

    loc,maxi,eV = LOC(file_path="Labo1/images Labo 1/DFB/DFB_10deg_40ma.txt")
    print("La longueur d'onde central de la DFB à 10C est de {loc} nm correspondant à {eV} eV, puissance de {maxi_lin} mW ({maxi_db}dBm)."
          .format(loc = round(loc,3),eV=round(eV,4),maxi_lin=round(maxi[0],4),maxi_db = round(maxi[1],2)))

if fwhm_DFB:
    fwhm_20 = FWHM(file_path="Labo1/images Labo 1/DFB/DFB_20deg_40ma.txt")
    print("La largeur mi-hauteur de la DFB à 20C est de {fwhm} pm."
          .format(fwhm = round(fwhm_20*1e3,5)))
    
    fwhm_10 = FWHM(file_path="Labo1/images Labo 1/DFB/DFB_10deg_40ma.txt")
    print("La largeur mi-hauteur de la DFB à 10C est de {fwhm} pm."
          .format(fwhm = round(fwhm_10*1e3,5)))

if slsr:
    slsr_20,low_20,center_20,high_20 = SLSR(file_path="Labo1/images Labo 1/DFB/DFB_20deg_40ma.txt")
    print("Le rapport de suppression des lobes secondaire de la DFB à 20C est de {slsr} dB."
          .format(slsr = round(min(slsr_20),2)))
    
    slsr_10,low_10,center_10,high_10 = SLSR(file_path="Labo1/images Labo 1/DFB/DFB_10deg_40ma.txt")
    print("Le rapport de suppression des lobes secondaire de la DFB à 10C est de {slsr} dB."
          .format(slsr = round(min(slsr_10),2)))
    
if fsr:
    slsr_20,low_20,center_20,high_20 = SLSR(file_path="Labo1/images Labo 1/DFB/DFB_20deg_40ma.txt")
    fsr = (center_20[0]-low_20[0]+high_20[0]-center_20[0])/2
    print("L'intervale spectrale de la DFB à 20C est d'environ {fsr} nm."
        .format(fsr = round(fsr,2)))


    slsr_10,low_10,center_10,high_10 = SLSR(file_path="Labo1/images Labo 1/DFB/DFB_10deg_40ma.txt")
    fsr = (center_10[0]-low_10[0]+high_10[0]-center_10[0])/2
    print("L'intervale spectrale de la DFB à 10C est d'environ' {fsr} nm."
        .format(fsr = round(fsr,2)))