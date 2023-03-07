with open(r'C:\Users\k_mir\OneDrive\Рабочий стол\PP2\Lab6\A.txt', 'r', encoding='utf-8') as f:
    with open(r'C:\Users\k_mir\OneDrive\Рабочий стол\PP2\Lab6\B.txt', 'w', encoding='utf-8') as k:
        a = f.read()
        k.write(a)