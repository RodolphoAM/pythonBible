import re

phoneList = open("phone_list.txt")
for line in phoneList:
    if re.search(r"^[jJ]", line):
        print(line)

phoneList.close()
