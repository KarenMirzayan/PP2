from math import sqrt
def prim(n):
    t = True
    if n > 1:
        for j in range(2, int(sqrt(n)) + 1):
            if n % j == 0:
                t = False
                break
    else:
        t = False
    return t
class FltrdPrim:
    lst = []
    def get(self):
        self.lst = [int(i) for i in input().split()]
    def prim(self):
        self.lst = list(filter(lambda x: prim(x), self.lst))

s = FltrdPrim()
s.get()
s.prim()
print(s.lst)
