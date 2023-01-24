x = "awesome" #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x) # >>> fantastic

myfunc()

print("Python is " + x) # >>> awesome






x = "awesome"

def myfunc():
  global x
  x = "fantastic" #make local "x" global

myfunc()

print("Python is " + x) # >>> fantastic