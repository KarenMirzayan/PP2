def uni(s):
    b = []
    for i in s:
        if i not in b:
            b.append(i)
    return b
s = [i for i in input().split()]
print(uni(s))