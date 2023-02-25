import re

s = input()
a = re.split(r'[A-Z]', s)
print(a)