# Prend un array de data et fait une image#
#Auteur : Philippe Arsenault
# Fonction solo qui prend une array de data et qui fait une image

import matplotlib.pyplot as plt
import random

# You have to use plt.show() at the end to get an image


def make_image(data, title,axe_x = [1500,1600,'titre de l\'axe x'], axe_y = [-100,0,'titre de l\'axe y'],label = 'Label oublié'): 
    #data is 2D array, title is string, axe_x is 3 member array with [start,end, label], label is curve legend label

    x_values = []
    y_values = []
    # Parse le data en un tableau en X et un tableau en Y

    for i in range(len(data[:])):
    # print(i)
        x_values.append(data[i][0])
        y_values.append(data[i][1])

    plt.title(title)
    plt.plot(x_values,y_values, linewidth = 3, color = new_color(), label = label)
    plt.xlabel(axe_x[2], fontsize=16)
    plt.ylabel(axe_y[2], fontsize=16)
    plt.legend()

# Randomize the color on the graph
def new_color():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return(color)

