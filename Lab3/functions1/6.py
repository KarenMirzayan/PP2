def rev(s):
    a = reversed(s.split())
    b = ''
    for i in a:
        b += i + " "
    return b
a = input()
print(rev(a))
    

