def rever(n):
    for i in range(n, -1, -1):
        yield i
for i in rever(10):
    print(i)
