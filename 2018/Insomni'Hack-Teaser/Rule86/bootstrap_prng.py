#!/usr/bin/env python3

# Bootstrapping PRNG
RULE = [86 >> i & 1 for i in range(8)]
N_BYTES = 32
N = 8 * N_BYTES

def next(x):
    x = (x & 1) << N+1 | x << 1 | x >> N-1
    y = 0
    for i in range(N):
        y |= RULE[(x >> i) & 7] << i
    return y

# Bootstrap the PNRG
keystream = 84607154736791766065800361525374060783583128122748167105652288627872379068488
for i in range(N//2):
    keystream = next(keystream)
print (keystream)
