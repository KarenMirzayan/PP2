class Shape:
    area = 0
    def Area(self):
        print(self.area)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = width * length
p = Rectangle(10, 5)
p.Area()

        