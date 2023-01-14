import os

# 1 task
os.chdir("C:/")

# 2 task
print(os.listdir())

# 3 task
try:
    os.chdir("Users")
except FileNotFoundError:
    raise Exception("Directory not found")


# 4 task
os.mkdir("new_folder")
os.rename("new_folder", "old_folder")
os.rmdir("old_folder")

# 5 task
files = os.listdir()
txt_files = [file for file in files if file.endswith(".txt")]
print(txt_files)
