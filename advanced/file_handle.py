#write
fileHandle = open('test.txt', 'w')
fileHandle.write("This is a test.\nReally, is it.")
fileHandle.close()
#append
fileHandle = open('test.txt', 'a')
fileHandle.write("\nBottom line.")
fileHandle.close()
#read
fileHandle = open('test.txt', 'r')
#print(fileHandle.read())
#print(fileHandle.readline())
fileLists = fileHandle.readlines()
for line in fileLists:
    print(line)
fileHandle.close()

fileHandle = open('testBinary.txt', 'wb')
fileHandle.write(str.encode("There is no spoon"))
fileHandle.close()

fileHandle = open('testBinary.txt', 'rb')
print(fileHandle.read())
fileHandle.close()

