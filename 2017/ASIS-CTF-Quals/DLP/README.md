# DLP

Challenge Points: 158

Ciphertext is generated as following:
```python
def encrypt(nbit, msg):
    msg = bytes_to_long(msg)
    p = getPrime(nbit)
    q = getPrime(nbit)
    n = p*q
    s = getPrime(4)
    enc = pow(n+1, msg, n**(s+1))
    return n, enc
```  
  
We know that enc = (n+1)<sup>msg</sup> mod n<sup>s+1</sup>  
Thus, according to Binomial Theorem we can write:  
The expansion of (n+1)<sup>msg</sup> is as follows:  
![equation](https://latex.codecogs.com/png.latex?\small&space;{msg\choose&space;0}n^{msg}&space;&plus;&space;{msg\choose&space;1}n^{msg-1}&space;&plus;&space;{msg\choose&space;2}n^{msg-2}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-1}n&space;&plus;&space;{msg\choose&space;msg}n^{0})  
And so we can also write,  
![equation](https://latex.codecogs.com/png.latex?\small&space;({msg\choose&space;0}n^{msg-2}&space;&plus;&space;{msg\choose&space;1}n^{msg-3}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-2})n^2&space;&plus;&space;{msg\choose&space;msg-1}n&space;&plus;&space;{msg\choose&space;msg}n^{0})  
Which can be written as,  
![equation](https://latex.codecogs.com/png.latex?\small&space;(x)n^2&space;&plus;&space;mn&space;&plus;&space;1) where,  
![equation](https://latex.codecogs.com/png.latex?\small&space;x&space;=&space;{msg\choose&space;0}n^{msg-2}&space;&plus;&space;{msg\choose&space;1}n^{msg-3}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-2})  
If we take the above result and **divide it with n^2**, the following can be written: ![equation](https://latex.codecogs.com/png.latex?\small&space;xn^2&space;&plus;&space;mn&space;&plus;&space;1&space;\equiv&space;mn&plus;1&space;\pmod&space;{n^2})  
Since, n<sup>s+1</sup> is always greater than and divisible by n<sup>2</sup>, we can now calculate the message `msg` as:  
![equation](https://latex.codecogs.com/png.latex?\small&space;enc&space;\equiv&space;(n&plus;1)^{msg}&space;\pmod&space;{n^{s&plus;1}})  
![equation](https://latex.codecogs.com/png.latex?\small&space;enc&space;\equiv&space;(msg*n&space;&plus;&space;1)&space;\pmod&space;{n^2})  
Therefore,  
![equation](https://latex.codecogs.com/png.latex?\small&space;msg&space;=&space;\frac{enc\%n^{2}&space;-&space;1}{n})  
  
Surprisingly, this is the single line exploit to the challenge: 
```python
from sage.all import *
hex(int((enc%n^2-1)/n))[2:].replace("L","").decode("hex")
```


