from math import sqrt
from time import sleep
n = int(input())
t = int(input()) / 1000
b = sqrt(n)
sleep(t)
print(f"Square root of {n} after {t} seconds is {b}")