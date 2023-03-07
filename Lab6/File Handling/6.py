import os

for i in "ABCDEFFGHIJKLMNOPQRSTUVWXYZ":
    k = i + '.txt'
    file_name = os.path.join(r'Lab6\File Handling', k)
    with open(file_name, "w") as file:
        file.write(file_name)