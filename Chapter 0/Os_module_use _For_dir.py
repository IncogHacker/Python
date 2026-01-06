import os

# Get the path of the directory you want to list
# Use '.' for current directory or replace with any path like 'C:/Users/YourName/Documents'

#? directory_path = '.' # current or Parent one we can also change it

directory_path="./Chapter 0"

# Get the list of all files and directories
try:
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory was not found.")
except PermissionError:
    print("Permission denied to access the directory.")
