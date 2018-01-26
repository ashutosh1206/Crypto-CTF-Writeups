from Crypto.Util.number import *
from hashlib import md5

flag = "AAAAAAAAAAAAAA"
assert len(flag) == 14
pad = bytes_to_long(md5(flag).digest())

hack = 0

for char in flag:
	hack+= pad
	hack*= ord(char)
	
print hack