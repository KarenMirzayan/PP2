class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1)
del p1.age
print(p1)
del p1