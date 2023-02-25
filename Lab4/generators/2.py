def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
s = []
for i in even(int(input())):
    s.append(i)
print(*s, sep = ', ')
