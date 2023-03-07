s = input().split()
with open(r"C:\Users\k_mir\OneDrive\Рабочий стол\PP2\Lab6\test.txt", 'w', encoding='utf-8') as f:
    for i in range(len(s) - 1):
        f.write(s[i] + " ")
    f.write(s[len(s) - 1])