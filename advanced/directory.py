import os
for fileName in os.listdir('./'):
    print (fileName)

os.mkdir('testDirectory')
os.rmdir('testDirectory')
