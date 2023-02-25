import re

s = input()
a = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(a)