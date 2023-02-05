class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, a, b):
        self.x += a
        self.y += b
    def dist(self, a, b):
        print((self.x - a) ** 2 + (self.y - b) ** 2)

        