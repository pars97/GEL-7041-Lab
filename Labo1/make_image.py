# Prend un array de data et fait une image#
# Auteur : Philippe Arsenault
# Fonction solo qui prend une array de data et qui fait une image

import matplotlib.pyplot as plt
import random

# You have to use plt.show() at the end to get an image


def make_image(data, title,axe_x = [1500,1600,'titre de l\'axe x'], axe_y = [-100,0,'titre de l\'axe y'],label = 'Label oublié', couleur = "FFAA22"): 
    #data is 2D array, title is string, axe_x is 3 member array with [start,end, label], label is curve legend label

    x_values = []
    y_values = []
    # Parse le data en un tableau en X et un tableau en Y

    for i in range(len(data[:])):
    # print(i)
        x_values.append(data[i][0])
        y_values.append(data[i][1])

    plt.title(title)
    plt.axis([axe_x[0],axe_x[1],axe_y[0],axe_y[1]])
    plt.plot(x_values,y_values, linewidth = 1, color = couleur, label = label)
    plt.xlabel(axe_x[2], fontsize=16)
    plt.ylabel(axe_y[2], fontsize=16)
    plt.legend()

# Randomize the color on the graph
def new_color(i):
    color =[]
    color.append("#FC0303")
    color.append("#FC7703")
    color.append("#FCE803")
    color.append("#56FC03")
    color.append("#03FCC6")
    color.append("#03F4FC")
    color.append("#0324FC")
    color.append("#6F03FC")
    color.append("#FC03B1")
    color.append("#DB03FC")
    return(color[i])

