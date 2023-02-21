def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for i in even(int(input())):
    print(i)
