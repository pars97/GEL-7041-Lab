#SLSR
# Auteur : Philippe Arsenault
# Prend un path du labo 1 et redonne le SLSR et les trois principaux peaks
from txt2data import txt2data

def SLSR(file_path):
    data_x,data_y  = txt2data(file_path=file_path)
    indice_centre = data_y.index(max(data_y))
    window_low = indice_centre-500
    window_high = indice_centre+500
    power_low = -120
    power_high = -120  

    for i in range(0,window_low):
        if power_low < data_y[i]:
            power_low = data_y[i]
            indice_low = i

    for j in range(len(data_y)-1,window_high-1,-1):
        if power_high < data_y[j]:
            power_high = data_y[j]
            indice_high = j

    #print(indice_centre)
    #print(indice_low)
    #print(data_x[indice_low],data_y[indice_low])
    #print(indice_high)
    #print(data_x[indice_high],data_y[indice_high]) 

    SLSR = [data_y[indice_centre]-data_y[indice_low],data_y[indice_centre]-data_y[indice_high]]
    low_peak = [data_x[indice_low],data_y[indice_low],indice_low]
    center_peak = [data_x[indice_centre],data_y[indice_centre],indice_centre]
    high_peak = [data_x[indice_high],data_y[indice_high],indice_high]

    return SLSR,low_peak,center_peak,high_peak