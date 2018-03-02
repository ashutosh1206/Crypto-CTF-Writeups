# RSAbaby
The idea behind the challenge involved knowledge of basic Number Theory which was pretty cool.  
  
We are given a couple of parameters and an encryption script which is used for encrypting the message. Everything in the script works normally except the `GenerateKeys` function:  
![picture](https://i.imgur.com/RdXt8bo.png)  
There is are two extra variables other than the regular public key parameters whose values are known: `g` and `h`  
  
I think the challenge creators left two different intentional vulnerabilities- one was bit by bit decryption and the other was a simple application of number theory. We discuss exploiting `g` using simple yet interesting application of number theory  

## The exploit
We know that:  
![equation](https://latex.codecogs.com/gif.latex?g=d*(p-0xdeadbeef))  
![equation](https://latex.codecogs.com/gif.latex?eg=ed*(p-0xdeadbeef))  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}=2^{ed*(p-0xdeadbeef)})  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}\mod&space;n=2^{ed*(p-0xdeadbeef)}\mod&space;n)  
Thus we can write,  
![equation](https://latex.codecogs.com/gif.latex?2^{ed*(p-0xdeadbeef)}=2^{(1&plus;k\phi(n))*(p-0xdeadbeef)})  
![equation](https://latex.codecogs.com/gif.latex?2^{(1&plus;k\phi(n))*(p-0xdeadbeef)}=(2*2^{k\phi(n)})^{(p-0xdeadbeef)})  
![equation](https://latex.codecogs.com/gif.latex?(2*2^{k\phi(n)})^{(p-0xdeadbeef)}=2^{(p-0xdeadbeef)}*2^{k*\phi(n)*(p-0xdeadebeef)})  
We know from Euler's Theorem that when GCD(a, n) == 1:  
![equation](https://latex.codecogs.com/gif.latex?a^{\phi(n)}\equiv1\mod&space;n)  
![equation](https://latex.codecogs.com/gif.latex?2^{(p-0xdeadbeef)}*2^{k*\phi(n)*(p-0xdeadebeef)}\equiv2^{p-0xdeadebeef}*1\mod&space;n)  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}\mod&space;n=2^{p-0xdeadbeef}\mod&space;n)  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}*2^{0xdeadbeef}\mod&space;n=2^{p}\mod&space;n)  
We know from Fermat's Little Theorem that when GCD(a, p) == 1:  
![equation](https://latex.codecogs.com/gif.latex?a^{p}\equiv&space;a\mod&space;n)  
We can now write:  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}*2^{0xdeadbeef}\mod&space;n&space;=&space;2)  
Thus,  
![equation](https://latex.codecogs.com/gif.latex?2^{eg}*2^{0xdeadbeef}\mod&space;n&space;-2)  
will be a factor of modulus N.  
We can easily get one of the factors of N as p = GCD(2^(eg + 0xdeadbeef) mod N - 2, N) and q = N/p  

## Exploit script
Checkout the complete exploit script [here](exploit.py)