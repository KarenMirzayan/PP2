def has_33(s):
    t = False
    for i in range(len(s) - 1):
        if s[i] == 3 and s[i + 1] == 3:
            t = True
            break
    return t
s = [int(i) for i in input().split()]
print(has_33(s))
