# FWHM
# Auteur : Philippe Arsenault
# Prend un path du labo 1 et redonne le FWHM. À noter que le half max en linéaire = -3dB

from txt2data import txt2data




def FWHM(file_path):
    data_x,data_y = txt2data(file_path=file_path)
    index_LOC = data_y.index(max(data_y))
    power_3dB  = max(data_y)-3
    mini = max(data_y)-min(data_y)

    # Part du milieu et va vers la droite en cherchant l'index du point le plus proche de -3db, si égal à -3db, escape la loop
    for i in range(index_LOC,len(data_y)):
        #print("i = {}".format(i))
        a = abs(data_y[i]-power_3dB)
        if mini == a:
            indice_up = i
            print("Valeur ==a, Break")
            break
        elif mini>a:
            mini = a
            indice_up = i
        else:
            pass

            

                
    mini = max(data_y)-min(data_y)
    # Part du milieu jusqu'au début et va vers la gauche en cherchant l'index du point le plus proche de -3db, si égal à -3db, escape la loop
    for j in range(index_LOC,-1,-1):
        #print("j = {}".format(j))
        b = abs(data_y[j]-power_3dB)
        if mini == b:
            indice_down = j
            print("Valeur ==b, Break")
            break
        elif mini>b:
            mini = b
            indice_down = j
        else:
            pass
    
    fwhm = data_x[indice_up]-data_x[indice_down]
    return (fwhm)


