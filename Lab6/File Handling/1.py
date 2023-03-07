import os

path = input("Enter path: ")

print("Directories:")
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)

print("\nFiles:")
for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        print(file_name)

print("\nAll directories and files:")
for file_dir_name in os.listdir(path):
    print(file_dir_name)