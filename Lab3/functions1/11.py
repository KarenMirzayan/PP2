def pal(s):
    a = []
    a.extend(s)
    b = list(reversed(a))
    if a == b:
        return True
    return False
a = input()
print(pal(a))