import re

s = input()
if re.findall(r"a\w+b", s):
    print(True)
else:
    print(False)