import timeit 
import numpy as np

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
    S = []
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        S.append(thisCoin)
        coin = coin - thisCoin

    return S


def makeChange(n, D):
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
                print("I can't find a solution")
                break
    return S


if __name__ == "__main__":
    amnts = [8,25,47,642,1025,356]
    clist = np.array([5,10,100,1,25])
    clist =  -np.sort(-clist)
    # clist = [100,25,10,5,1]


    f= open("data","w+")
    print("greedy algorithm:")
    for amnt in amnts:
        coinsUsed = [0]*(amnt+1)
        coinCount = [0]*(amnt+1)
        start= 0
        end = 0
        start = timeit.timeit()
        dpMakeChange(clist,amnt,coinCount,coinsUsed)
        end = timeit.timeit()
        Ss = printCoins(coinsUsed,amnt)
        print(Ss , len(Ss))
        f.write(str(end) +  ", ")

    f.write("\n")


    for amnt in amnts:
        start= 0
        end = 0
        start = timeit.timeit()
        S = makeChange(amnt, clist)
        end = timeit.timeit()
        print(S , len(S))
        f.write(str(end) +  ", ")

    f.write("\n")


    clist = np.array([6,4,1])
    clist =  -np.sort(-clist)

    for amnt in amnts:
        coinsUsed = [0]*(amnt+1)
        coinCount = [0]*(amnt+1)
        start= 0
        end = 0
        start = timeit.timeit()
        dpMakeChange(clist,amnt,coinCount,coinsUsed)
        end = timeit.timeit()
        Ss = printCoins(coinsUsed,amnt)
        print(Ss , len(Ss))
        f.write(str(end) +  ", ")

    f.write("\n")


    for amnt in amnts:
        start= 0
        end = 0
        start = timeit.timeit()
        S = makeChange(amnt, clist)
        end = timeit.timeit()
        print(S , len(S))
        f.write(str(end) +  ", ")

    f.write("\n")

    f.close()

    # print("Making change for",amnt,"requires")
    # print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    # print("They are:")
    # Ss = printCoins(coinsUsed,amnt)
    # print(Ss , len(Ss))

    # S = makeChange(amnt, clist)
    # print(S , len(S))