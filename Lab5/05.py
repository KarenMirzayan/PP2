import re

s = input()
x = re.findall(r"a\w+b", s)
print(x)