import numpy as np
import matplotlib.pyplot as plt

nb_decimale = 7

A = ["Foyer Objet",np.array([1,1.15]) , "m"] #exemple : nom de la variable, valeurs, unité(s)
B = ["Volume",np.array([12,24]) , "mL"]
C = ["Concentration",np.array([0.001,0.002]) , "mol"]

serie = 1 #variable muette
for i in A,B,C :

    nom = i[0]
    valeurs = i[1] #Changement de la variable à étudier
    unite = i[2]

    #affichage des stats
    print("----","SERIE",serie,":",nom,"----")
    print("Nombre de mesures :",len(valeurs))
    print("Etendue :",max(i[1])-min(i[1]))
    print("Médiane :", np.median(valeurs))
    print("Valeur moyenne :", np.mean(valeurs) , unite)
    print("Ecart-type:", round(np.std(valeurs,ddof=1), nb_decimale) ,unite)
    print("Incertitude-type:", round(np.std(valeurs,ddof=1) /(len(valeurs))**0.5, nb_decimale) ,unite)
    print("Incertitude élargie, 95% :",round( 2* np.std(valeurs,ddof=1) /(len(valeurs))**0.5, nb_decimale) ,unite)
    print()
    serie += 1

#Affichage du graphique

for i in A,B,C :
    plt.figure()
    plt.hist(i[1],bins = 'rice')
    plt.title("Histogramme des valeurs")
    plt.xlabel("mesures")
    plt.ylabel("Fréquences")
    
    
plt.show()
        