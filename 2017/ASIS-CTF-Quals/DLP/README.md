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
  
Thus, according to Binomial Theorem we can write:
enc = (n+1)<sup>msg</sup> mod n<sup>s+1</sup>
The expansion of (n+1)<sup>msg</sup> is as follows:  
![equation](https://latex.codecogs.com/png.latex?{msg\choose&space;0}n^{msg}&space;&plus;&space;{msg\choose&space;1}n^{msg-1}&space;&plus;&space;{msg\choose&space;2}n^{msg-2}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-1}n&space;&plus;&space;{msg\choose&space;msg}n^{0})  
And so,  
![equation](https://latex.codecogs.com/gif.latex?({msg\choose&space;0}n^{msg-2}&space;&plus;&space;{msg\choose&space;1}n^{msg-3}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-2})n^2&space;&plus;&space;{msg\choose&space;msg-1}n&space;&plus;&space;{msg\choose&space;msg}n^{0})  
Which can be written as,  
![equation](https://latex.codecogs.com/png.latex?(x)n^2&space;&plus;&space;mn&space;&plus;&space;1)  
where ![equation](https://latex.codecogs.com/gif.latex?x&space;=&space;{msg\choose&space;0}n^{msg-2}&space;&plus;&space;{msg\choose&space;1}n^{msg-3}&space;&plus;&space;...&space;&plus;&space;{msg\choose&space;msg-2})  
If we take the above result and **divide it with n^2**, we can write:  
![equation](https://latex.codecogs.com/gif.latex?(xn^2&space;&plus;&space;mn&space;&plus;&space;1)&space;\%&space;n^2&space;=&space;mn&space;&plus;&space;1)  
We can now calculate the message `msg` as:  


