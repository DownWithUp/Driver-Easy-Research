import urllib.request

custom_headers = {'User-Agent' : 'DriverEasy/Free V5.6.7.42416 snmdD41D8CD98F00B204E9800998ECF8427E',  # hard-coded user agent
                  'Content-Type' : 'text/plain; encoding=uft-8'}
UPLOAD_XML_URL = "http://app1.drivereasy.com/NewDriver/GetNewDriver"

strFilePath = input("Path of Encrypted XML file to send: ")
hFile = open(strFilePath, 'rb+')
bFileData = hFile.read()
hFile.close()
userRequest = urllib.request.Request(UPLOAD_XML_URL, bFileData, headers=custom_headers)
response = urllib.request.urlopen(userRequest)
hFile = open(strFilePath + ".OUT", 'wb+')
hFile.write(response.read())
hFile.close()
