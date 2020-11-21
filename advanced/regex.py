import re

x = re.search("cat", "A cat and a mouse cannot be friends")
print(x)

x = re.search("cow", "A cat and a mouse cannot be friends")
print(x)

x = re.search(r"M[ae][iy]er", "Meyer")
print(x)
x = re.search(r"M[ae][iy]er", "Maier")
print(x)
x = re.search(r"M[ae][iy]er", "Herman")
print(x)
