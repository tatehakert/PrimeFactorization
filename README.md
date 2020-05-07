Welcome to the RSA encryption cracker!

Run the file main.py with no arguments to see the efficiency of the trivial method of prime factorization versus 
the more efficient version using Pollard's rho algorithm. 

The main.py program will also go through the process of generating a public/private key 
pair using hard coded prime numbers which are hard coded (you can change them if you like).

Using the public key from the previous step, my program will attempt to determine the corresponding private key 
using Pollard's rho method of prime factorization

The largest semiprime this program has managed to factor is: 
   
    n = 2722258935367507717705132147404722668699
        p = 36893488147419103363 
        q = 73786976294838206473
    
    Using Pollard's rho algorithm took (3.4 hours)
 

This program has other functions built in to allow you to encrypt and decrypt messages using public and private keys
Their usage can be seen in main.py 
