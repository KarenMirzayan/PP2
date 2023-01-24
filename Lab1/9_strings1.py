# "" == ''
print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# """ == '''
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1]) # >>> e

for x in "banana":
    print(x) # every letter on different line, "x" is iterator

#length == len()
a = "Hello, World!"
print(len(a))

# is lesser str in bigger str
txt = "The best things in life are free!"
print("free" in txt) # >>> True

txt = "The best things in life are free!"
if "free" in txt: #True
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt) # >>> True

txt = "The best things in life are free!"
if "expensive" not in txt: #True
  print("No, 'expensive' is NOT present.")