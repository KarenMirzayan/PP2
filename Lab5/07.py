import re

s = input()
a = re.sub(r'(_)(?P<A>.)', lambda x: x.group("A").upper(), s)
print(a)