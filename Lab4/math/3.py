from math import tan, radians
n = int(input())
angles = (180 - 360/n)/2
a = int(input())
ctg = 1/tan(radians(angles))
area = round(n * (a**2)/(4*ctg))
print(area)