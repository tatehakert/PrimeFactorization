import math
import time
from itertools import count
from math import gcd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# ---------------- Functions -----------------

def getPrimesBetween(start, end):
    primesList = []
    for index in range(start, end + 1):              # (index) from start to end + 1
        if index > 1:
            for f in range(2, index // 2 + 2):       # (f) from 2 to floor(val/2) + 2
                if index % f == 0:
                    break
                else:
                    if f == index // 2 + 1:
                        primesList.append(index)

    return primesList



def isPrime(n):
    if n > 3:
        halfN = math.ceil(n/2)
        for i in range(2, halfN):
            if n % i == 0:
                return 0

        return 1
    else:
        return 1


def findFactors1(num):
    n = num
    sqrtN = math.ceil(math.sqrt(n))
    print("sqrtN: ",sqrtN)
    trivial_factors = []


    for f in range(2, sqrtN+1):

        while n % f == 0:
            n = int(n / f)
            trivial_factors.append(f)
        if n == 1:
            break

    if n != 1 and isPrime(n):
       trivial_factors.append(n)

    print("prime factors of ", num, ": ", *trivial_factors)
    return trivial_factors



#Pollard’s rho algorithm:  This algorithm factors a number n=pq. It works by generating a sequence of pseudorandom numbers using a function:
#g(x) = (x2 + 1) mod n
#Starting with x = y = 2, in each iteration we calculate:
# x = g(x) and y = g(g(y)),
# then we calculate the d = gcd((x - y), n).
# if(d != 1) → then d is a nontrivial factor of n


def pRho(num, i):
    n = num
    x = i
    y = i
    d = 1
    custom_factors = []
    product = 1

    while d == 1:
        x = ((x * x) + 1) % num
        y = ((y * y) + 1) % num
        y = ((y * y) + 1) % num

        d = math.gcd(abs(x - y), num)

        if d != 1:
            custom_factors.append(int(d))
            if num % d != 0:
                print("ERROR: num %", d, " != 0")

            n = int(n // d)
            custom_factors.append(int(n))
            break

    if d != num:
        print("factors of ", num, ": ", *custom_factors)

        if custom_factors[0] * custom_factors[1] != num:
            print("ERROR: factors to not multiply to num")
            print("next i for pRho: ", i + 1)
            return pRho(num, i+1)
        return custom_factors
    else:
         print("next i for prho: ", i + 1)
         return pRho(num, i +1)

def makeSemiPrimeList():
    primeSet1 = getPrimesBetween(10000000, 10005000)
    primeSet2 = getPrimesBetween(20000000, 20005000)
    semiPrimeSet = []
    if len(primeSet1) <= len(primeSet2):
        for i in range(1, len(primeSet1)):
            semiPrimeSet.append(primeSet1[i] * primeSet2[i])
    else:
        for i in range(1, len(primeSet2)):
            semiPrimeSet.append(primeSet1[i] * primeSet2[i])


    with open('semiPrimes2.txt', 'w') as file:
        for semiPrime in semiPrimeSet:
            file.write('%s\n' % semiPrime)

def readInSemiPrimes(fileName):
    semiPrimeList = []
    with open(fileName, 'r') as file:
        for line in file:
            # remove '/n' which is the last character of the line
            semiPrime = int(line[:-1])
            semiPrimeList.append(semiPrime)
        return semiPrimeList


# ---------------- MAIN -----------------








