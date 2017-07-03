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

def first16bytes(listm):
    list16 = list()
    if len(listm)>16:
        i=0
        while i<16:
            list16.append(listm.pop(0))
            i+=1
        return list16
    else:
        while len(listm)<16:
            listm.append('')
        return listm

gost =gost2015(k)

newFile = open(filenameout, "wb")
newFile.close()

newFile = open(filenameout, "ab")


while len(message)>16:
    print ("-----------")
    m = first16bytes(message)
    print (m)
    print ("+++++++++++++++")
    c = gost.decryption(m)
    newFileBytes = c
    newFileByteArray = bytearray(newFileBytes)

    newFile.write(newFileByteArray)
    print (c)

print ("-----------")
print (first16bytes(message))
print ("+++++++++++++++")
c = gost.decryption(m)
newFileBytes = c
newFileByteArray = bytearray(newFileBytes)

newFile.write(newFileByteArray)
print (c)







newFileBytes = c
newFileByteArray = bytearray(newFileBytes)

newFile.write(newFileByteArray)
newFile.close()



