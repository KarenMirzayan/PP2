import re
s = input()
x = re.findall(r"[A-Z]_[a-z]+", s)
print(x)