from itertools import permutations
def perm(s):
    a = [].extend(s)
    b = permutations(a)
    for i in list(b):
        for j in i:
            print(j, end = '')
        print()
s = input()
perm(s)