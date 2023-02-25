import re

s = input()
a = re.sub(r'(?:_)(.)', lambda x: x.group(1).upper(), s)
print(a)