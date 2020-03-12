import numpy as np 


def returnChange(n, D):
    S = []
    suma = 0
    i = 0 
    x = 0
    while (suma != n):
        x = D[i]
        if (x+suma <=n):
            suma += x
            S.append(x)
        else: 
            i += 1
            if(i > D.size - 1):
                print("No encuentro solucion")
                break
    return S


D = np.array([5,10,100,1,25])
D =  -np.sort(-D)

S = returnChange(157, D)

print(S , len(S))