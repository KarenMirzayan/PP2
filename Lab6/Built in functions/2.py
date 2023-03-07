s = input()
s = list(filter(lambda x: x.isalpha(), s))
u = len(list(filter(lambda x: x.isupper(), s)))
l = len(s) - u

print("Upper:", u)
print("Lower:", l)