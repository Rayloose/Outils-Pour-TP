import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

N = 10**3
nb_decimale = 5
X = ["Volume", np.array([12, 24, 32, 44]), "L", 2] 
Y = ["Quantité de CO2 dégagé", np.array([0.1, 0.2, 0.4, 0.7]), "mol", 0.01]

# exemple : nom de la variable, valeurs, unité(s), incertitudes en forme de liste ou valeur unique

a = np.zeros(N)
b = np.zeros(N)

for i in range(N):
    Xi = rd.normal(X[1], X[3])
    Yi = rd.normal(Y[1], Y[3])
    a[i], b[i] = np.polyfit(Xi, Yi, 1)

print('regression linéaire de type Y = AX + B')
print("A :", round(a.mean(),nb_decimale),"+-",round(a.std(),nb_decimale))
print(" B :", round(b.mean(),nb_decimale),"+-",round(b.std(),nb_decimale))

plt.errorbar(X[1],Y[1], xerr= X[3], yerr = Y[3])
plt.xlabel("à compléter")
plt.ylabel("à compléter")
plt.plot(Xi, Xi*a.mean()+b.mean(), label="Regression")
plt.show()
