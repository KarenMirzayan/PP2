def myfunc(n):
    x = (i for i in range(n) if i % 3 == 0 and i % 4 == 0)
    return x
s = myfunc(100)
for i in s:
    print(i)