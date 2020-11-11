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

fileMode = fileStats(stat.ST_MODE)

if stat.S_ISREG(fileStats[stat.ST_MODE]):
    print("Regular file")
elif stat.S_ISDIR((fileStats[stat.ST_MODE])):
    print("Directory")
elif stat.S_ISLNK((fileStats[stat.ST_MODE])):
    print("Shortcut")
elif stat.S_ISSOCK((fileStats[stat.ST_MODE])):
    print("Socket")
elif stat.S_ISFIFO((fileStats[stat.ST_MODE])):
    print("Named pipe")
elif stat.S_ISBLK((fileStats[stat.ST_MODE])):
    print("Block special device")
elif stat.S_ISCHR((fileStats[stat.ST_MODE])):
    print("Character special device")
