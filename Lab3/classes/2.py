class Shape:
    area = 0
    def Area(self):
        print(self.area)
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area = length ** 2
p = Square(10)
p.Area()
