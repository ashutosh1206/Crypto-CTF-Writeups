from Crypto.Util.number import *
import random
from flag import FLAG

def generate(nbits):
	p = getPrime(nbits)
	q = getPrime(nbits)
	n = p * q * p
	g = random.randint(1, n)
	h = pow(g, n, n)
	return (n, g, h)

def encrypt(m, n, g, h):
	r = random.randint(1, n)
	c = pow(pow(g, m, n) * pow(h, r, n), 1, n)
	return c

m = [ord(char) for char in FLAG]
n, g, h = generate(90)
open("pubkey.txt", "w").write("{0}:{1}:{2}".format(n, g, h))

c = [encrypt(mi, n, g, h) for mi in m]
open("enc.txt", "w").write(str(c))
