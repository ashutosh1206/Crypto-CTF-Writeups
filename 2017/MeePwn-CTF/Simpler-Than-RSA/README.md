# Simpler Than RSA
  
Challenge Points: 100  
  
We are given an encryption script [simple.py](simple.py). Values of n, g, h are public other than the ciphertext. The following function is used to generate values for the challenge:  
![picture](https://i.imgur.com/0QUHha4.png)  
The encryption function:  
![picture](https://i.imgur.com/ORlFqDf.png)  
As we can see, the ciphertext for each character in the plaintext is generated separately. For the `ith` byte of message we can write the corresponding ciphertext as:  
![equation](https://latex.codecogs.com/gif.latex?c_i=((g^{m_i}\mod&space;n)*(h^{r}\mod&space;n))\mod&space;n)  
Given: ![equation](https://latex.codecogs.com/gif.latex?h=g^{n}\mod&space;n)  
We can now write:  
![equation](https://latex.codecogs.com/gif.latex?c_i=((g^{m_i}\mod&space;n)*(g^{nr}\mod&space;n))\mod&space;n)  
which gives us ![equation](https://latex.codecogs.com/gif.latex?c_i=g^{m_i&plus;nr}\mod&space;n)  
Since n=p*p*q,  
![equation](https://latex.codecogs.com/gif.latex?c_i=g^{m_i&plus;p^{2}qr}\mod&space;n)  
Raising both sides by (p-1)*(q-1), we have:  
![equation](https://latex.codecogs.com/gif.latex?c_i^{(p-1)*(q-1)}\mod&space;n=g^{(m_i&plus;p^{2}qr)*(p-1)*(q-1)}\mod&space;n)  
![equation](https://latex.codecogs.com/gif.latex?c_i^{(p-1)*(q-1)}\mod&space;n=g^{(m_i*(p-1)*(q-1))&plus;(p*(p-1)*(q-1)*nr)}\mod&space;n)  
Since phi(n) = p*(p-1)*(q-1),  
![equation](https://latex.codecogs.com/gif.latex?c_i^{(p-1)*(q-1)}\mod&space;n=(g^{(m_i*(p-1)*(q-1))}*g^{nr\phi(n)})\mod&space;n)  
Euler's theorem states that when GCD(a, n) == 1: ![equation](https://latex.codecogs.com/gif.latex?a^{\phi(n)}\equiv1\mod&space;n)  
We can now write,  
Equation(a): ![equation](https://latex.codecogs.com/gif.latex?c_i^{(p-1)*(q-1)}\mod&space;n=g^{m_i*(p-1)*(q-1)}.1\mod&space;n)  
We have now eliminated `r` from the equation, let us first get the factors of n, trying it on [factordb.com](factordb.com) gives us the factors as:  
```
    p = 1057817919251064684989791981
    q = 1103935256393984899021164397
```  
Now that we have the factors, we can use Equation(a) to get solution for each ciphertext byte. For each byte, we just have to check for 256 possibilities of corresponding message byte and a total of 54*256 brute-force checks to get the flag(We already know the other values in Equation(a): p,q,ciphertext byte). The exploit:  
```python
list1 = open("enc.txt",'r').read()[1:-2]
list1 = list1.split(",")
list1 = [int(i[:-1]) for i in list1]
list1 = [pow(i, (p-1)*(q-1), n) for i in list1]
msg = ""
for i in list1:
	for j in range(1, 256):
		if pow(g, j*(p-1)*(q-1), n) == i:
			msg += chr(j)
	print msg
```  
This gives us the flag: MeePwnCTF{well_is_fact0rizati0n_0nly_w4y_to_s0lve_it?}  
Check out the entire exploit script [here](exploit.py)

