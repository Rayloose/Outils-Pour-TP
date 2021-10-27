import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

N = 10**3
A = ["Volume",np.array([12,24,32,44]) , "L"] #exemple : nom de la variable, valeurs, unité(s)
B = ["Incertitude Volume",np.array([1,1.15,0.2,4]) , "L"]
C = ["Concentration",np.array([0.1,0.2,0.4,0.7]) , "mol"]
D = ["Incertitude concentration",np.array([0.01,0.02,0.05,0.07]) , "mol"]

X = A[1]
u_X = B[1]
Y = C[1]
u_Y = D[1]

a = np.zeros(N)
b = np.zeros(N)

for i in range(N):
    Xi = rd.normal(X, u_X)
    Yi = rd.normal(Y, u_Y)
    a[i] , b[i] = np.polyfit(Xi, Yi, 1)
    
print("Valeur moyenne pour A:", a.mean())
print("Incertitude-type sur A :", a.std())
print("Valeur moyenne pour B:", b.mean())
print("Incertitude-type sur B :", b.std())

plt.plot(Xi,Yi, label="Valeurs avec tirages")
plt.plot(Xi,Xi*a.mean()+b.mean(),label = "Regression")
plt.show()
