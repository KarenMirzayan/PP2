import os

file_path = input()

if not os.path.exists(file_path):
    print(f"{file_path} does not exist.")
    exit()

if not os.access(file_path, os.W_OK):
    print(f"You do not have permission to delete {file_path}.")
    exit()

os.remove(file_path)
print(f"{file_path} has been deleted.")