import numpy as np
import matplotlib.pyplot as plt

VX = np.array([1,2,3]) #Valeurs de x
VY = np.array([2,3,4]) #Valeurs de y
IX = np.array([0.1,0.1,0.1]) #Incertitudes sur x
IY = np.array([0.1,0.1,0.1]) #Incertitudes sur y

if len(VX) != len(VY) or len(IX) != len(IY) or len(VX)!= len(IX) :
    print("Taille des listes non homogène")
    
x = VX
y = VY
xi = IX 
yi = IY
 
opt, cov = np.polyfit(x,y,1,cov=True) #degree du polynome

print("Y = AX+B")
print("A=",opt[0],"+-",cov[0,0]**0.5)
print("B=",opt[1],"+-",cov[1,1]**0.5)

plt.errorbar(x,y,xerr = xi, yerr=yi)
plt.plot(x,opt[0]*x+opt[1],color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title("Régression linéaire")
plt.show()