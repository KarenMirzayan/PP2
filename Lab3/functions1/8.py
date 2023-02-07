def spy_game(s):
    a = 0
    t = False
    for i in range(len(s)):
        if s[i] == 0:
            a += 1
        if s[i] == 7 and a >= 2:
            t = True
    if t:
        return True
    return False
s = [int(i) for i in input().split()]
print(spy_game(s))