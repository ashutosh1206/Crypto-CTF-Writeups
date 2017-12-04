# Gracias (Crypto, 287p)

```
Some people think that combination of cryptographic systems will definitely improve the security. That’s your turn to prove them wrong.
```

In this task, we get [encryption script](gracias.py) to exploit upon.
The task is not really difficult as it looks like. The challenge is to break the given multi-prime based RSA encryption.

A few steps in the encryption: 
1. Private and Public keys are generated using the same function `make_pubpri(nbit)` 
    a. The function generates primes `p` , `q` and `r` like conventional RSA encryption
    b. Along with public keys `n` and `e`, the function also generates a 2*nbit safe prime number `a` and another number `g` following the criteria given below
    c. So, the public key actually contains `n`, `e`, `a`, `g` and the private key contains `n`, `d`, `a`, `g`
2. The encryption function `encrypt(m, pub)` works as follows:
    a. Using the public key generated in Step-1, it generates two numbers k and K as `k = getRandomRange(2, a)` and `K = pow(g, k, a)`
    b. Now, instead of encrypting the message `m` using the public keys, it does the following operation to get ciphertext `c1` and `c2`:
        (i) `c1, c2 = pow(k, e, n), (m * K) % a`
    c. Returns `c1` and `c2` as ciphertext

The attack on this will work as follows:
1. Using `c1`, `e` and `n`, get the value of `k` 
2. Calculate `K` using `k` generated in Step-1
3. Finally calculate message `m` as `m = (c2 * (k^(-1) mod n)) mod n`

A direct Wiener's Attack will not work in this case since it doesn't exactly follow the criteria of `d` being less than `N^(1/4)`.

You can check this variant of Wiener Attack which works when the size of `d` is just a few bits greater than `N^(1/4)`. Paper on a variant of Wiener Attack [here](https://www.math.tugraz.at/~cecc08/abstracts/cecc08_abstract_20.pdf).

Conclusion from the paper which is significant for exploit of this challenge:
1. Along with d being the denominator of the convergent of the continued fraction of (e/n), the decryption exponent can also be written in the form:
    a. `d = r*q(m+1) + s*q(m)`

Here q(m+1) and q(m) are the (m+1)th and mth denominators of the convergents of the continued fraction of (e/n) respectively.

This is a script implementing the above conclusion:
'''python
def wiener(e, n):
	m = 12345
	c = pow(m, e, n)
	q0 = 1

	list1 = continued_fraction(Integer(e)/Integer(n))
	conv = list1.convergents()
	for i in conv:
		k = i.numerator()
		q1 = i.denominator()

		for r in range(20):
			for s in range(20):
				d = r*q1 + s*q0
				m1 = pow(c, d, n)
				if m1 == m:
					return d
		q0 = q1
'''
which will give us the decryption exponent:
`d = 100556095937036905102538523179832446199526507742826168666218687736467897968451`

Then we can write the following code to get the flag: 
```python
from Crypto.Util.number import *
 
k = pow(c1, d, n)
K = pow(g, k, a)
print long_to_bytes(c2 * inverse(K, a) % a)
```

This gives us the flag: `ASIS{Wiener_at7ack_iN_mUlt1_Prim3_RSA_iZ_f34sible_t0O!}`

If you want to check how I approached the challenge in detail, checkout my blog [here](https://masterpessimistaa.wordpress.com/2017/11/24/asis-finals-ctf-2017-gracias-writeup/)
The complete exploit script [here](exploit.py)


