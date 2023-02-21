def squares(a, b):
    for i in range(a, b+1):
        yield i * i
for i in squares(10, 20):
    print(i)