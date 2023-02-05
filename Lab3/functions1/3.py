def solve(numheads, numlegs):
    r = (numlegs - numheads * 2)/2
    c = numheads - r
    return f"There are {int(r)} rabbits and {int(c)} chickens"
a, b = int(input()), int(input())
print(solve(a, b))