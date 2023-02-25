import re

s = input()
a = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
print(a)