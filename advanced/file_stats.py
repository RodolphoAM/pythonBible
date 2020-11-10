import os
import stat
import time
fileStats = os.stat('test.txt')
fileInfo = {
    'Size': fileStats[stat.ST_SIZE],
    'LastModified': time.ctime(fileStats[stat.ST_MTIME]),
    'LastAcessed': time.ctime(fileStats[stat.ST_ATIME]),
    'CreationTime': time.ctime(fileStats[stat.ST_CTIME]),
    'Mode': time.ctime(fileStats[stat.ST_MODE])
}
for infoField in fileInfo:
    print("%s: %s"%(infoField, fileInfo[infoField]))
if stat.S_ISDIR(fileStats[stat.ST_MODE]):
    print("Directory.")
else:
    print("New directory")
