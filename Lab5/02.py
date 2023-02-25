import re
s = input()
x = re.findall(r"ab{2,3}", s)
print(x)