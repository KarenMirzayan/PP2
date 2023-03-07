import os

path = input()
if os.path.exists(path):
    print("Basename: " + os.path.basename(path) + '\n' + "Dirname: " + os.path.dirname(path))
else:
    print("Path does not exist.")
