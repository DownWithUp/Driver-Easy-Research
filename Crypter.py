from urllib import request
import urllib, platform, zlib, base64
# Coded for Python 3
strStaticKey = "39096799Easy" # From DriverEasy.exe

def fullDecypt(strFilePath):
	try:
		hFile = open(strFilePath, 'rb+')
	except:
        print("[!] Error opening file")
        return
    bData = hFile.read()
    strOut = ""
    for i in range(len(bData)):
        cValue = bData[i]
        cTempValue = cValue ^ int(ord(strStaticKey[i % len(strStaticKey)]))
        strOut += chr(cTempValue)
    bData = base64.b64decode(strOut)
    # Helpful: https://stackoverflow.com/questions/1838699/how-can-i-decompress-a-gzip-stream-with-zlib
    bData = zlib.decompress(bData, 15 + 32)
    hFile.seek(0)
    hFile.truncate(0) # clear file
    hFile.write(bData)
    hFile.close()

def fullEncrypt(strFilePath):
    try:
        hFile = open(strFilePath, 'rb+')
    except:
        print("[!] Error opening file")
        return
    bData = hFile.read()
    zlibObj = zlib.compressobj(-1, zlib.DEFLATED, 31, 8, zlib.Z_DEFAULT_STRATEGY)
    bData = zlibObj.compress(bData)
    bData += zlibObj.flush()
    bData = base64.b64encode(bData)
    strOut = ""
    for i in range(len(bData)):
        cValue = bData[i]
        cValue = cValue ^ int(ord(strStaticKey[i % len(strStaticKey)]))
        strOut+= chr(cValue)
    bData = bytes(strOut, 'UTF-8')
    hFile.seek(0)
    hFile.truncate(0) # clear file
    hFile.write(bData)
    hFile.close()

# Main Body of the Code
print("Running under python:", platform.python_version())
cValue = input("Press [E] for Encryption and [D] for Decryption: ")
if(cValue.upper() == 'E'):
    strFilePath = input("Enter full file path: ")
    fullEncrypt(strFilePath)
elif(cValue.upper() == 'D'):
    strFilePath = input("Enter full file path: ")
    fullDecypt(strFilePath)
else:
    print("[!] Invalid choice: " + cValue)
quit()
