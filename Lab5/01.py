import re

s = input()
if re.search(r"ab*", s):
    print(True)
else:
    print(False)
