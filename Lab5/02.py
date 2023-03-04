import re

s = input()
if re.findall(r"ab{2,3}", s):
    print(True)
else:
    print(False)