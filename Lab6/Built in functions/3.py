s = input()
a = [i for i in reversed(s)]
a = ''.join(a)
print(a == s)