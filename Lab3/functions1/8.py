def spy_game(s):
    t = False
    for i in range(len(s) - 2):
        if s[i] == 0 and s[i + 1] == 0 and s[i + 2] == 7:
            t = True
            break
    return t
s = [int(i) for i in input().split()]
print(spy_game(s))