def pgcd(a, b):
    a, b = abs(a), abs(b)
    while b > 0:
        re = r(a, b)
        a, b = b, re
    return a

def q(a, b):
    q, r = a//b, a % b
    if r > b or r < 0:
        r -= b
        q += 1
    return int(q)

def r(a, b):
    r = a % b
    if r > b:
        r -= b
    elif r < 0:
        r += b
    return int(r)

def dioph_smart(a, b):
    if pgcd(a, b) != 1:
        return "pas de solution entières"

    quot = [] #Stocker les quotients et reste de la division euclidienne
    reste = []
    compteur = -1 #Initialiser à -1 car la division prends une étape en plus
    a_init = a
    b_init = b 
    L = []
    rs = abs(a) + abs(b)

    while b != 0 :
        quot.append(q(a, b))
        reste.append(r(a, b))
        a, b = b, reste[-1]
        compteur += 1

    #Méthode avec les formules en mains

    if compteur == 1 :      #Pour réduire considérablement la complexité du programme (peut-être à améliorer)
        return 1,   quot[0]
    if compteur == 2 :
        return  quot[1], 1+  quot[0]*quot[1]
    if compteur == 3 :
        return 1 +  quot[1]*quot[2], -quot[0]-quot[2]-quot[0]*quot[1]*quot[2]
    if compteur == 4:
        return -quot[1]-quot[3]-quot[1]*quot[2]*quot[3], 1 + quot[0]*quot[1] + quot[0]*quot[3] + quot[2]*quot[3] \
        + quot[0]*quot[1]*quot[2]*quot[3]
    if compteur > 4 :

    #Méthode brut force

        for u in range(-rs, rs):
            for v in range(-rs, rs):
                if (a_init*u)+(b_init*v) == 1:
                    L.append((u, v))

        return L[int(len(L)/2)],'brut force'

def parité(n):
    if n % 2 == 0:
        return "pair"
    else:
        return "impair"

def dioph_brut_force_smart(a,b,c = 1):
    if c % pgcd(a, b) != 0:
        return "pas de solution entières"
    L = []
    r = abs(a) + abs(b)
    compteur = 0

    for u in range(-r, r):
        u_p = parité(u)
        for v in range(-r, r):
            if u_p == parité(v) and (a*u)+(b*v) == c:
                L.append((u, v))

    return L[int(len(L)/2)]


    


