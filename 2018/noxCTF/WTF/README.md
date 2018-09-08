# WTF

**Challenge Points**: 742  
  
**Challenge Description**: Um uhhhhhhhhh WTF IS THIS?! I give up. Now you try to solve this.  
  
*Disclaimer*: Guessing involved in this challenge, so proceed at your own risk
  
In this challenge we are given N, e, c like every other RSA challenge, except for the fact that the values are encoded using some weird encoding technique. Googling about it leads to nothing, here are the public key values and ciphertext  

```
N = "lObAbAbSBlZOOEBllOEbblTlOAbOlTSBATZBbOSAEZTZEAlSOggTggbTlEgBOgSllEEOEZZOSSAOlBlAgBBBBbbOOSSTOTEOllbZgElgbZSZbbSTTOEBZZSBBEEBTgESEgAAAlAOAEbTZBZZlOZSOgBAOBgOAZEZbOBZbETEOSBZSSElSSZlbBSgbTBOTBSBBSOZOAEBEBZEZASbOgZBblbblTSbBTObAElTSTOlSTlATESEEbSTBOlBlZOlAOETAZAgTBTSAEbETZOlElBEESObbTOOlgAZbbOTBOBEgAOBAbZBObBTg"
e = "lBlbSbTASTTSZTEASTTEBOOAEbEbOOOSBAgABTbZgSBAZAbBlBBEAZlBlEbSSSETAlSOlAgAOTbETAOTSZAZBSbOlOOZlZTETAOSSSlTZOElOOABSZBbZTSAZSlASTZlBBEbEbOEbSTAZAZgAgTlOTSEBEAlObEbbgZBlgOEBTBbbSZAZBBSSZBOTlTEAgBBSZETAbBgEBTATgOZBTllOOSSTlSSTOSSZSZAgSZATgbSOEOTgTTOAABSZEZBEAZBOOTTBSgSZTZbOTgZTTElSOATOAlbBZTBlOTgOSlETgTBOglgETbT"
c = "SOSBOEbgOZTZBEgZAOSTTSObbbbTOObETTbBAlOSBbABggTOBSObZBbbggggZZlbBblgEABlATBESZgASBbOZbASbAAOZSSgbAOZlEgTAlgblBTbBSTAEBgEOEbgSZgSlgBlBSZOObSlgAOSbbOOgEbllAAZgBATgEAZbBEBOAAbZTggbOEZSSBOOBZZbAAlTBgBOglTSSESOTbbSlTAZATEOZbgbgOBZBBBBTBTOSBgEZlOBTBSbgbTlZBbbOBbTSbBASBTlglSEAEgTOSOblAbEgBAbOlbOETAEZblSlEllgTTbbgb"
```

Looking at such a big value of `e`, it had to be Wiener's Attack or it's variant. But we cannot move further without decoding the values.  
  

The part below is purely guessing  

So, one of my teammates suggested looking at the distinct characters in the encoded strings. Here are the distinct characters present in the encoded strings:  
> ['A', 'b', 'E', 'g', 'l', 'O', 'S', 'B', 'T', 'Z']

10 distinct characters, 10 digits in decimal system. So, each character represents a digit. But how do we map them?  
> 'O' --> 0  
> 'l' --> 1  
> 'Z' --> 2  
> 'E' --> 3  
> 'A' --> 4  
> 'S' --> 5  
> 'b' --> 6  
> 'T' --> 7  
> 'B' --> 8  
> 'g' --> 9  

Now, there is nothing significant left in the challenge, all that is left is to implement a simple Wiener's Attack, for which I wrote a sage/python implementation and got the flag:  
```python
from sage.all import *
from Crypto.Util.number import *

def mapping(str1):
    for i in str1:
        if i not in "AbEglOSBTZ":
            print i
    str1 = str1.replace("O", '0')
    str1 = str1.replace("l", '1')
    str1 = str1.replace("Z", '2')
    str1 = str1.replace("E", '3')
    str1 = str1.replace("A", '4')
    str1 = str1.replace("S", '5')
    str1 = str1.replace("b", '6')
    str1 = str1.replace("T", '7')
    str1 = str1.replace("B", '8')
    str1 = str1.replace("g", '9')
    return str1

def wiener(e, n):
    m = 12345
    c = pow(m, e, n)
    lst = continued_fraction(Integer(e)/Integer(n))
    conv = lst.convergents()
    for i in conv:
        k = i.numerator()
        d = int(i.denominator())
        try:
            m1 = pow(c, d, n)
            if m1 == m:
                print "[*] Found d: ", d
                return d
        except:
            continue
    return -1

N = "lObAbAbSBlZOOEBllOEbblTlOAbOlTSBATZBbOSAEZTZEAlSOggTggbTlEgBOgSllEEOEZZOSSAOlBlAgBBBBbbOOSSTOTEOllbZgElgbZSZbbSTTOEBZZSBBEEBTgESEgAAAlAOAEbTZBZZlOZSOgBAOBgOAZEZbOBZbETEOSBZSSElSSZlbBSgbTBOTBSBBSOZOAEBEBZEZASbOgZBblbblTSbBTObAElTSTOlSTlATESEEbSTBOlBlZOlAOETAZAgTBTSAEbETZOlElBEESObbTOOlgAZbbOTBOBEgAOBAbZBObBTg"
e = "lBlbSbTASTTSZTEASTTEBOOAEbEbOOOSBAgABTbZgSBAZAbBlBBEAZlBlEbSSSETAlSOlAgAOTbETAOTSZAZBSbOlOOZlZTETAOSSSlTZOElOOABSZBbZTSAZSlASTZlBBEbEbOEbSTAZAZgAgTlOTSEBEAlObEbbgZBlgOEBTBbbSZAZBBSSZBOTlTEAgBBSZETAbBgEBTATgOZBTllOOSSTlSSTOSSZSZAgSZATgbSOEOTgTTOAABSZEZBEAZBOOTTBSgSZTZbOTgZTTElSOATOAlbBZTBlOTgOSlETgTBOglgETbT"
c = "SOSBOEbgOZTZBEgZAOSTTSObbbbTOObETTbBAlOSBbABggTOBSObZBbbggggZZlbBblgEABlATBESZgASBbOZbASbAAOZSSgbAOZlEgTAlgblBTbBSTAEBgEOEbgSZgSlgBlBSZOObSlgAOSbbOOgEbllAAZgBATgEAZbBEBOAAbZTggbOEZSSBOOBZZbAAlTBgBOglTSSESOTbbSlTAZATEOZbgbgOBZBBBBTBTOSBgEZlOBTBSbgbTlZBbbOBbTSbBASBTlglSEAEgTOSOblAbEgBAbOlbOETAEZblSlEllgTTbbgb"
N = int(mapping(N))
e = int(mapping(e))
c = int(mapping(c))

d = wiener(e, N)
print long_to_bytes(pow(c, d, N))
```
In case you want to learn Wiener's Attack, you can learn about it on Crypton [here](https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-Wiener).  
  
Running this script gives us the flag as: **noxCTF{RSA_1337_10rd}**.