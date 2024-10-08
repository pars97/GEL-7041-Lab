# Longueur d'onde centrale
# Auteur : Philippe Arsenault
# Prend un path du labo 1 et redonne la longueur d'onde centrale, sa puissance (mW et dB), et sa bande interdite
from txt2data import txt2data
import scipy.constants as cte


def LOC(file_path):
    data_x,data_y = txt2data(file_path=file_path)
    index = data_y.index(max(data_y))
    LOC = data_x[index]
    maxi = [10**(max(data_y)/10),max(data_y)]
    eV = cte.h*cte.c/(LOC*1e-9)/cte.e
    return LOC,maxi,eV


