# Prime Enigma
  
**Challenge Points**: 50(+ 100)  
  
**Challenge Description**: Hey there fellow lizard how nice of you to drop by! Did you know those filthy humans really think that some numbers have special meanings? Seven, 13 and for some strange reason even 9000. Go and show them that a good prime does not make a secure cryptosystem!  
  
The following encryption is taking place:  
```python
g = 5
d = key
m = int(flag.encode('hex'), 16) % p

B = pow(g, d, p)  # Equation-1
k = pow(A, d, p)  # Equation-2
c = k * m % p     # Equation-3
```
Values p, A, g, B, c are known.  
**Encryption System**: ElGamal  
  
Prerequisites:  
1. Cyclic Groups
2. Discrete Logarithm Problem
3. Basic Number Theory
In case you are interested in understanding the exploit, but don't have much knowledge about Cyclic Groups and DLP, you can read about it here on my blog post: [Cyclic Groups, DLP and Baby Step Giant Step Algorithm](https://masterpessimistaa.wordpress.com/2018/01/14/dlp-and-baby-step-giant-step-algorithm/).
  
The entire exploit summed up:
1. We need to calculate the value of `d` by solving `Equation-1`
2. Calculate `k` using the value of `d` obtained from Step-1 in order to solve `Equation-2`
3. Calculate m = c * mod_inv(k, p) using the value of `k` obtained from Step-2 in order to solve `Equation-3`

**Solving Step-1**:  
We know from the property of Cyclic Groups that ![equation](https://latex.codecogs.com/png.latex?g^{|G|}&space;\equiv&space;1&space;\mod&space;p), where `|G|` is the cardinality/order of the Cyclic Group `G`. Cardinality i.e. the number of elements in the Cyclic Group, in this case, is `p-1`. Therefore we can write: ![equation](https://latex.codecogs.com/png.latex?g^{p-1}&space;\equiv&space;1&space;\mod&space;p) which is also known as [Fermat's Little Theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem).  
  
Note that B = p-1, which makes solving DLP a lot easier. We can now write:  
![equation](https://latex.codecogs.com/png.latex?p-1\equiv&space;g^d&space;\mod&space;p)  
which can also be written as:  
![equation](https://latex.codecogs.com/png.latex?g^d\equiv&space;-1&space;\mod&space;p)  
Upon squaring, we have:  
![equation](https://latex.codecogs.com/png.latex?g^{2d}\equiv&space;1&space;\mod&space;p)  
Comparing the above equation with ![equation](https://latex.codecogs.com/png.latex?g^{p-1}&space;\equiv&space;1&space;\mod&space;p), we can write:  
**d = (p-1)/2**   
  
**Solving Step-2**:  
Simple compute: ![equation](https://latex.codecogs.com/png.latex?k&space;=&space;A^d&space;\mod&space;p)  
  
**Solving Step-3**:  
Simply compute: ![equation](https://latex.codecogs.com/png.latex?m&space;=&space;ck^{-1}&space;\mod&space;p)  
  
Checkout the entire exploit script [here](exploit.py)
