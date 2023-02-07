from itertools import permutations
def perm(s):
    a = []
    a.extend(s)
    b = permutations(a)
    for i in set(b):
        for j in i:
            print(j, end = '')
        print()
s = input()
perm(s)