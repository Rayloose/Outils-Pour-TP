import numpy as np
import matplotlib.pyplot as plt

A = [] 
B = [] 
C = [] 

Ve = C #Changement de la variable à étudier
unite = "mL"

moy_Ve=np.mean(Ve) #Moyenne
sigma_Ve=np.std(Ve,ddof=1) #Ecart-type
u_Ve= sigma_Ve /(len(Ve))**0.5 #Incertitude-type

#affichage des stats

print("Nombre de mesures : ",len(Ve))
print("Valeur moyenne : ",moy_Ve,unite)
print("Ecart-type:",sigma_Ve,unite)
print("Incertitude-type:",u_Ve,unite)
print("Incertitude élargie, 95% :",2*u_Ve,unite)

#Affichage du graphique

plt.figure(figsize=(12,12))
plt.hist(Ve,bins=25,range=(49,50))
plt.title("Histogramme des valeurs")
plt.xlabel("mesure")
plt.ylabel("Fréquence")
plt.show()