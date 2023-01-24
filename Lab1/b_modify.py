# .upper() == convert to upper
a = "Hello, World!"
print(a.upper())

# .lower() == to lower
a = "Hello, World!"
print(a.lower())

# Use .strip() to delete spaces from both ends
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace every H to J (Case-sensitive)
a = "Hello, World!"
print(a.replace("H", "J"))

# .split() to split string into list by key inside function, default is " "
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']