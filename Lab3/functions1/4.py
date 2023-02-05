from math import sqrt
def prim(s):
    b = s
    for i in s:
        if i > 1:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    b.remove(i)
                    break
        else:
            b.remove(i)
    return b
s = [int(i) for i in input().split()]
print(*prim(s))