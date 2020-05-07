import math
from math import gcd
import random
from findFactors import pRho
#from findFactors import pRho

# -------------------- Functions --------------------
def modInverse(e, phi):
    # e * d ==   1  mod phi
    #     d == 1/e  mod phi
    #     d == e^-1 mod phi
    g, x, y = extendedGCD(e, phi)
    if g != 1:
        raise Exception("modular inverse not found")
    else:
        return x % phi


def extendedGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - (b // a) * y, y)



def generateKeyPair(p, q, e):
    print("Generating new public/private key pair with (p, q) = (", p, ", ", q, "):\n")
    n = p * q
    phi = (p-1)*(q-1)

    if e == -1:
        e = random.randrange(1, phi)

        greatestCommonDivisor = gcd(e, phi)

        # if e is not coprime to phi, set to random and check again until coprime
        while greatestCommonDivisor != 1:
            e = random.randrange(1, phi)
            greatestCommonDivisor = gcd(e, phi)


    d = modInverse(e, phi)


    print("p:   ", p)
    print("q:   ", q)
    print("n:   ", n)
    print("phi: ", phi)
    print("e:   ", e)
    print("d:   ", d)
    print("\n|///////////////////////////////////////////////////////////////////////////////////////////////////////|\n")
    print("Public  key (e, n): (", e, ", ", n, ")")
    print("Private key (d, n): (", d, ", ", n, ")")
    print("\n|///////////////////////////////////////////////////////////////////////////////////////////////////////|\n")

    return ((e, n),(d, n))

def encryptPlaintext(plaintext, pk):
    key, n = pk

    #convert each letter of the plaintext to a int representing the unicode character
    intRepresentation = [ord(char) for char in plaintext]
    print("intRepresentation: ", intRepresentation)

    hexRepresentation = [hex(ord(char))[2:] for char in plaintext]
    print("hexRepresentation: ", hexRepresentation)
    bigHexRep = ''.join(map(lambda x: str(x), hexRepresentation))
    print("bigHexRep: ", bigHexRep)

    #then raise each int to the power of key and calculate the result mod n
    cipher = []
    for char in plaintext:
        #c = (ord(char) ** key) % n
        #c = ord(char) * key
        c = pow(ord(char), key, n)
        print("c: ", c)
        cipher.append(c)

    return cipher

def encrypt(pt, pk):
    key, n = pk

    cipher =  [hex(pow(ord(char),key,n))[2:] for char in pt]

    return cipher

def decrypt(ciphertext, pk):
    key, n = pk

    plaintext = [chr(pow(int(char,16), key, n)) for char in ciphertext]

    return plaintext

def crackPublicKey(pk):
    e, n = pk

    primeFactors = pRho(n, 2)
    print("factors: ", *primeFactors)
    publicKey, privateKey = generateKeyPair(primeFactors[0], primeFactors[1], e)

    return privateKey


def crackEncryption(cipher, pk):
    e, n = pk
    factors = pRho(n, 2)
    print("factors: ", *factors)
    publicKey, privateKey = generateKeyPair(factors[0], factors[1], e)

    return decrypt(cipher, privateKey)



