# BabyCrypt (Crypto, 350)

This challenge was a bit overrated, there were no complications in the challenge, as you will see when we discuss the writeup.

In this challenge, we are supposed to get the flag which is present in the server. The server has an input-output program running, which gives AES-ECB encryption of the input given to it. The encryption takes place as follows: 
1. Takes the input from the user
2. Appends `secret` (which is the flag here) to the input
3. Pads to make it a multiple of blocksize
4. Encrypts the resultant string using AES in ECB mode
5. Gives the ciphertext as the output

As you can see, we are only in control of the input which we are supposed to give to the server. Using the input that we give, we need to get the `secret` which is the flag.
Let us have a look at how the blocks are divided when we send an input of size equal to the blocksize (16 in this case): 
```
        1st Block | 2nd Block | 3rd Block | ...
        Input     | Secret    | secret+padding ...
```
The first block contains 16 bytes of our input, which is known to us. When we send an input of size one less than the blocksize, then the block division is as follows:
```
        1st Block | 2nd Block    | 3rd Block | ...
        x         | Secret[1:17] | secret[17:]+padding ...
```
Here `x = 15 bytes input + 1 byte secret`.
We know the first 15 bytes of block #1, we can simply brute force 256 possibilities of the 16th byte in block #1 by checking the corresponding ciphertexts of block #1.

For the second byte we send 14 random bytes + 1 byte of secret(we got from previous step) as the input to the server and then brute force for 2nd byte of secret which again has 256 possibilties. We keep on continuing this process to get each byte of the secret and finally get the flag:
`flag{Crypt0_is_s0_h@rd_t0_d0...}`

In case you want to know how I approached the problem in detail, checkout my blogpost [here](https://amritabi0s.wordpress.com/2017/09/18/csaw-quals-2017-babycrypt-writeup/).
Check my complete exploit script for this challenge [here](exploit.py).