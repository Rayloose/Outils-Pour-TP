from os import name
import numpy as np
import matplotlib.pyplot as plt



A = ["Foyer Objet",np.array([1,1.15]) , "m"] #exemple : nom de la variable, valeurs, unité(s)
B = ["Foyer image",np.array([12,24]) , "mL"]
C = ["Foyer",np.array([0.001,0.002]) , "mol"]

a = 1

for i in A,B,C :

    valeurs = i[1] #Changement de la variable à étudier
    unite = i[2]

    #affichage des stats
    print("----","SERIE",a,"----")
    print("Nombre de mesures : ",len(valeurs))
    print("Etendue : ",max(i[1])-min(i[1]))
    print("Médiane :", np.median(valeurs))
    print("Valeur moyenne : ", np.mean(valeurs) , unite)
    print("Ecart-type:", np.std(valeurs,ddof=1) ,unite)
    print("Incertitude-type:", np.std(valeurs,ddof=1) /(len(valeurs))**0.5 ,unite)
    print("Incertitude élargie, 95% :",2* np.std(valeurs,ddof=1) /(len(valeurs))**0.5 ,unite)
    print()
    a += 1

    #Affichage du graphique


for i in A,B,C :

    plt.hist(i[1])
    plt.title("Histogramme des valeurs")
    plt.xlabel("mesures")
    plt.ylabel("Fréquences")
    plt.show()

        