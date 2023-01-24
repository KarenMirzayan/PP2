x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Spaces must-have
# "+" is oveloaded, both sum and concatenation
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

# Can't add int and str
"""
x = 5
y = "John"
print(x + y)
"""

# Do this instead
x = 5
y = "John"
print(x, y)
