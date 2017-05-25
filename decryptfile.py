from symmetric.gost import gost2015
import binascii
import sys

if __name__ == "__main__":
    key = sys.argv[1]
    filenamein = sys.argv[2]
    filenameout = sys.argv[3]

k = list(binascii.unhexlify(key))

message = list()

with open(filenamein, 'rb') as f:
   while 1:
       byte_s = f.read(1)
       if not byte_s:
           break
       byte = byte_s[0]
       message.append(byte)

f.close()
gost =gost2015(k)

d = gost.decryption(message)

newFileBytes = d
newFileByteArray = bytearray(newFileBytes)

newFile = open(filenameout, "wb")
newFile.write(newFileByteArray)
newFile.close()

