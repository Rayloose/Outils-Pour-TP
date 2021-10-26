import numpy as np
import matplotlib as plt

x = np.array([0,2,4])
xi = np.array([1,2,3]) #Incertitudes

y = np.array([0.1,0.1,0.1])
yi = np.array([0.1,0.1,0.1]) #Incertitudes

opt, cov = np.polyfit(x,y,1,cov=True) #degree du polynome

print("a=",opt[0],"+-",cov[0,0]**0.5)
print("a=",opt[1],"+-",cov[1,1]**0.5)

plt.pyplot.errorbar(x,y,xerr = xi, yerr=yi)
plt.plot(x,opt[0]*x+opt[1],color="red")
plt.xlabel(x)
plt.ylabel(y)
plt.grid()
plt.title("Régression linéaire")
plt.savefig("droite.png")