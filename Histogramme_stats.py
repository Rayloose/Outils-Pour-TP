import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,2,3]) 
B = [] 
C = [] 

valeurs = A #Changement de la variable à étudier
Valeur_attendu = 1
unite = "mL"

moy_valeurs=np.mean(valeurs) #Moyenne
sigma_valeurs=np.std(valeurs,ddof=1) #Ecart-type
u_valeurs= sigma_valeurs /(len(valeurs))**0.5 #Incertitude-type

#affichage des stats

print("Nombre de mesures : ",len(valeurs))
print("Valeur moyenne : ",moy_valeurs,unite)
print("Ecart-type:",sigma_valeurs,unite)
print("Incertitude-type:",u_valeurs,unite)
print("Incertitude élargie, 95% :",2*u_valeurs,unite)
print("Z-score",abs(np.mean(valeurs)-Valeur_attendu)/u_valeurs)

#Affichage du graphique

plt.hist(valeurs)
plt.title("Histogramme des valeurs")
plt.xlabel("mesure")
plt.ylabel("Fréquence")
plt.show()