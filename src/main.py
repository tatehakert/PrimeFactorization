import time

from simpleRSA import generateKeyPair
from simpleRSA import encrypt
from simpleRSA import decrypt
from simpleRSA import crackEncryption
from simpleRSA import crackPublicKey

from findFactors import readInSemiPrimes
from findFactors import findFactors1
from findFactors import pRho
# -------------------- MAIN --------------------

print("Welcome to the RSA encryption cracker!\n")
#publicKey, privateKey = generateKeyPair(35184372088891, 70368744177679, -1)            #2^45, 2^46   <-- time to crack:     11.90, 12.23
#publicKey, privateKey = generateKeyPair(70368744177679, 140737488355333, -1)           #2^46, 2^47   <-- time to crack:     13.84, 13.86
#publicKey, privateKey = generateKeyPair(140737488355333, 281474976710677, -1)          #2^47, 2^48   <-- time to crack:     14.04, 13.40
#publicKey, privateKey = generateKeyPair(281474976710677, 562949953421381, -1)          #2^48, 2^49   <-- time to crack:     27.46, 25.39
#publicKey, privateKey = generateKeyPair(562949953421381, 1125899906842679, -1)         #2^49, 2^50   <-- time to crack:     22.88, 23.46
#publicKey, privateKey = generateKeyPair(1125899906842679, 2251799813685269, -1)        #2^50, 2^51   <-- time to crack:     22.46,  22.98
#publicKey, privateKey = generateKeyPair(2251799813685269, 4503599627370517, -1)        #2^51, 2^52   <-- time to crack:     94.07,  96.32
#publicKey, privateKey = generateKeyPair(4503599627370517, 9007199254740997, -1)        #2^52, 2^53   <-- time to crack:     118.97, 117.70
#publicKey, privateKey = generateKeyPair(9007199254740997, 18014398509482143, -1)       #2^53, 2^54   <-- time to crack:     122.42	123.47
#publicKey, privateKey = generateKeyPair(18014398509482143, 36028797018963971, -1)      #2^54, 2^55   <-- time to crack:     40.71,  44.87
#publicKey, privateKey = generateKeyPair(36028797018963971, 72057594037928017, -1)      #2^55, 2^56   <-- time to crack:     42.58,  43.73
#publicKey, privateKey = generateKeyPair(72057594037928017, 144115188075855881, -1)     #2^56, 2^57   <-- time to crack:     241.06, 251.12
#publicKey, privateKey = generateKeyPair(144115188075855881, 288230376151711813, -1)    #2^57, 2^58   <-- time to crack:     251.15
#-
#publicKey, privateKey = generateKeyPair(18014398509482147, 36028797018963979, -1)      #2^54, 2^55   <-- time to crack:     367.14
#publicKey, privateKey = generateKeyPair(36028797018963979, 72057594037928033, -1)      #2^55, 2^56   <-- time to crack:     450.93
#publicKey, privateKey = generateKeyPair(72057594037928033, 144115188075855907, -1)     #2^56, 2^57   <-- time to crack:     729
#publicKey, privateKey = generateKeyPair(144115188075855907, 288230376151711813, -1)    #2^57, 2^58   <-- time to crack:     481.19
#-
#publicKey, privateKey = generateKeyPair(288230376151711813, 576460752303423619, -1)    #2^58, 2^59   <-- time to crack:     491.58
#publicKey, privateKey = generateKeyPair(576460752303423619, 1152921504606847009, -1)   #2^59, 2^60   <-- time to crack:     1705.47
#publicKey, privateKey = generateKeyPair(1152921504606847009, 2305843009213693967, -1)  #2^60, 2^61   <-- time to crack:
#publicKey, privateKey = generateKeyPair(2305843009213693967, 4611686018427388039, -1)  #2^61, 2^62   <-- time to crack:     2632.14
#publicKey, privateKey = generateKeyPair(9223372036854775837, 18446744073709551629, -1)  #2^63, 2^64   <-- time to crack:    1806.9
#publicKey, privateKey = generateKeyPair(36893488147419103363, 73786976294838206473, -1)  #2^65, 2^66   <-- time to crack:    12282.25
"""
messageToEncrypt = "hello there"
print("\nMessage to encrypt: ", messageToEncrypt)

print("\nPublic key encryption: ")
cipher = encrypt(messageToEncrypt, publicKey)
print("\n  message encrypted using public key")
print("     cipher: ", ''.join(map(str, cipher)) )

plaintext = decrypt(cipher, privateKey)
print("\n  message decrypted using private key")
print("     plaintext: ", ''.join(map(str, plaintext)) )


print("\nPrivate key encryption: ")
cipher = encrypt(messageToEncrypt, privateKey)
print("\n  message encrypted using private key")
print("     cipher: ", ''.join(map(str, cipher)) )

plaintext = decrypt(cipher, publicKey)
print("\n  message decrypted using public key")
print("     plaintext: ", ''.join(map(str, plaintext)) )


print("\n----------------------------------------------------")
print("\n\nNow to crack the encryption!")
print("We will again encrypt a message using the public key and decrypt the message using only the public key\n")

newMessage = "We hacked RSA!"
print("messageToEncrypt: ", newMessage)

cipher = encrypt(newMessage, publicKey)
print("\n  message encrypted using public key")
print("     cipher: ", ''.join(map(str, cipher)) )
"""
"""
print("\n---Attempting to extract private key from public key---\n")

start = time.time()
crackedPrivateKey = crackPublicKey(publicKey)

print("SUCCESS! We cracked the public key!")
print("     private key: ", crackedPrivateKey)
end = time.time()

#print("\n  message cracked using only the public key")
#print("     plaintext: ", ''.join(map(str, plaintext)) )
print("time to crack: ", (end - start))


"""

semiPrimeSet = readInSemiPrimes('semiPrimes3.txt')
labels = semiPrimeSet
trivial_times = []
custom_times = []

results = dict() # semiPrime: {"custom_time": 0, 'custom_factors': [], "trivial_time": 0, 'trivial_factors': [],}

for semiPrime in semiPrimeSet:
    print("\nsemiPrime: ", semiPrime)
    results[semiPrime] = {'custom_factors': [], 'custom_time': 0, 'trivial_factors': [], 'trivial_time': 0}

    start = time.time()
    results[semiPrime]['custom_factors'] =  pRho(semiPrime, 2)
    end = time.time()
    results[semiPrime]['custom_time'] = round(end - start, 4)
    custom_times.append(round(end - start,4))

    start = time.time()
    results[semiPrime]['trivial_factors'] = findFactors1(semiPrime)
    end = time.time()
    results[semiPrime]['trivial_time'] = round(end - start,4)
    trivial_times.append(round(end - start,4))

for semiPrime in results:
    print("\nsemiPrime: ", semiPrime)
    print(" trivial_factors: ", *results[semiPrime]['trivial_factors'], " trivial_time: ", results[semiPrime]['trivial_time'])
    print(" custom_factors: ",  *results[semiPrime]['custom_factors'],  " custom_time: ",  results[semiPrime]['custom_time'])


