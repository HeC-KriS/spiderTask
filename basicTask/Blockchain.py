theSecret = 25
import random

#function to create Polynomial
def generatePolynomial(n,code):
    poly = {}
    poly['a0'] = code
    for i in range(1,n+1):
        poly[f'a{str(i)}']=random.randint(1,9999999)
    return poly
#function to generate shares for a specific polynomian
def generateShares(poly,N):
    k = len(poly)
    shares = {}
    for i in range(N):
        x = random.randint(1,10)
        y=0
        for j in range(0,k):
            y += poly[f'a{j}']*(x**j)
        shares[x] = y
    return shares
#creating polynomial
poly = generatePolynomial(6,theSecret)
#generating 12 shared
shares = generateShares(poly,12)
print(poly)
print(shares)
#function to find the secret no.
def findCode(partOfShares):
    x = list(partOfShares.keys())
    y = list(partOfShares.values())
    k = len(x)
    codeGuess = 0

    for i in range(k):
        li = 1
        for j in range(k):
            if i != j:
                li *= (0 - x[j]) / (x[i] - x[j])
        codeGuess += y[i] * li

    return round(codeGuess)
print(findCode(dict(list(shares.items())[:7])))
#printing the secret number

print(findCode(shares))
