from Crypto.PublicKey import *

key = RSA.importKey(open("publickey.pem").read())
print "Modulus: ", key.n
print "Public Key exponent: ", key.e