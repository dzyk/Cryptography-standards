import unittest
from publickey.ec import ECPoint
from symmetric.belt import belt
from symmetric.dstu import dstu2014
from symmetric.gost import gost2015
from publickey.dstu4145 import DSTU4145
from publickey.gost import DSGOST
from publickey.stb import reverse, STB
import binascii
import sys

if __name__ == "__main__":
    key = sys.argv[1]
    filename = sys.argv[2]

k = list(binascii.unhexlify(key))
f = open(filename, "rb")

with open(filename, 'rb') as f:
   while 1:
       byte_s = f.read(1)
       if not byte_s:
           break
       byte = byte_s[0]
       print("byte-%s"%byte)

f.close()

def test_gost_enc(self):
    mtest = list(binascii.unhexlify('1122334455667700ffeeddccbbaa9988'))
    ktest = list(binascii.unhexlify('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'))
    gost =gost2015(ktest)
    c = gost.encryption(mtest)

def test_gost_dec(self):
    mtest = list(binascii.unhexlify('1122334455667700ffeeddccbbaa9988'))
    ktest = list(binascii.unhexlify('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'))
    gost =gost2015(ktest)
    c = gost.encryption(mtest)
    d = gost.decryption(c)
