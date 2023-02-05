from math import sqrt
def prim(s):
    if s > 1:
        for j in range(2, int(sqrt(s)) + 1):
            if s % j == 0:
                return False
    return True
s = [int(i) for i in input().split()]
a = filter(prim, s)
print(list(a))