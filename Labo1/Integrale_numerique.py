# Integrale_numerique
# Auteur : Philippe Arsenault
# it takes the filepath from labo1 and spits out the linear total power and dBm 
from txt2data import txt2data
import math

def numeric_integral(file_path):
    data_x,data_y = txt2data(file_path=file_path)
    data_y_lin = []
    sum = 0
    dx = data_x[1]-data_x[0]

    for i in range(len(data_y)):
        data_y_lin.append(10**(data_y[i]/10)) #Réponse en mW


    for i in range(len(data_y_lin)):
        sum = sum + data_y_lin[i]*dx

    return (sum, 10*math.log(sum,10))