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
   byte_s = f.read()
   message = list(byte_s)

print (message)
f.close()
gost =gost2015(k)
c = gost.encryption(message)
print (c)


newFileBytes = c
newFileByteArray = bytearray(newFileBytes)

newFile = open(filenameout, "wb")
newFile.write(newFileByteArray)
newFile.close()

