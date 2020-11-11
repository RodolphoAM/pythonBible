import fnmatch
import os
import re

filePattern = fnmatch.translate('*.txt')

for fileName in os.listdir('./'):
    if re.match(filePattern, fileName):
        print("Text file")

    if fnmatch.fnmatch(fileName, '?.txt'):
        print("Text file")

    if fnmatch.fnmatch(fileName, '*.txt'):
        print(open(fileName).read())
    elif fnmatch.fnmatch(fileName, '?.txt'):
        print("Text file")
    elif fnmatch.fnmatch(fileName, '*.exe'):
        print(fileName)

import glob
for fileName in glob.glob('[0-9].txt'):
    print("Text file")
