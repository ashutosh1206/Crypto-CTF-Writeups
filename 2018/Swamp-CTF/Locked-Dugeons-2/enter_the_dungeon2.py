#!/usr/bin/env python2.7

from hashlib import sha256, md5
from Crypto.Cipher import AES
import os
import random
from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
import sys

BLOCK_SIZE = 16
KEY = os.urandom(16)
IV = os.urandom(16)

pad_len = lambda inp: (BLOCK_SIZE - len(inp) % BLOCK_SIZE)
pad = lambda inp: inp + chr(pad_len(inp))*pad_len(inp)
unpad = lambda inp: inp[:-ord(inp[-1])]

class AESCipher:
    def __init__(self, key):
        self.key = sha256(key).digest()

    def __encrypt(self, _str, iv):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_str = pad(_str)
        return cipher.encrypt(padded_str)
    
    def encrypt_wrapper(self, _str, iv):
        return b64encode(iv + self.__encrypt(_str, iv))

    def __decrypt(self, enc_str, iv):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_str = cipher.decrypt(enc_str)
        decrypted_str = unpad(decrypted_str)
        return decrypted_str

    def decrypt_wrapper(self, encoded_enc_str):
        enc_str = b64decode(encoded_enc_str)
        return self.__decrypt(enc_str[16:], enc_str[:16])

if __name__ == "__main__":
    with open("flag.txt") as fd:
        flag = fd.read()
    flag_size = len(flag)

    key=KEY
    insertion_range = flag_size//BLOCK_SIZE
    insertion_position = random.randrange(insertion_range)*BLOCK_SIZE
    mod_flag = flag[:insertion_position] + "send_modflag_enc" + flag[insertion_position:]
    
    aescipher = AESCipher(key)
    enc_mod_flag = aescipher.encrypt_wrapper(mod_flag, IV)
    sys.stdout.write(enc_mod_flag)
    sys.stdout.write('\n')
    sys.stdout.flush()
    next_level = False
    
    for i in range(insertion_range):
        sys.stdout.write("What do you want me to do?\n")
        sys.stdout.flush()
        enc_recv_str = raw_input()
        dec_recv_str = aescipher.decrypt_wrapper(enc_recv_str)
        if "get_modflag_md5" in dec_recv_str:
            next_level = True
            sys.stdout.write("Dungeon goes deeper..\n")
            sys.stdout.flush()
            break
        else:
            sys.stdout.write("I am gonna ask again!\n")
            sys.stdout.flush()

    if next_level:
        len_enc_mod_flag = len(enc_mod_flag)
        inp_size_limit = int(len_enc_mod_flag*4/3) + 50
        for i in xrange(500):
            enc_recv_str = raw_input()
            if len(enc_recv_str) > inp_size_limit:
                continue
            dec_recv_str = aescipher.decrypt_wrapper(enc_strrecv_str)
            sys.stdout.write(b64encode(md5(dec_recv_str).digest()))
            sys.stdout.write("\n")
            sys.stdout.flush()