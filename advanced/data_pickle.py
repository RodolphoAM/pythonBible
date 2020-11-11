import pickle
fileHandle = open('pickleFile.pikcle', 'wb')
testList = [123, {'Calories': 190}, 'Mr Anderson.', [1, 2, 7]]
pickle.dump(testList, fileHandle)
fileHandle.close()
#unpickling  the data is just as easy
fileHandle = open('pickleFile.pikcle', 'rb')
print(pickle.load(fileHandle))
fileHandle.close()
