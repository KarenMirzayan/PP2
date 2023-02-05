def hist(s):
    for i in s:
        print('*' * i)
a = [int(i) for i in input().split()]
hist(a)