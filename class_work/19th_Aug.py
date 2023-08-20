# file = open("newfile.txt", "r")

# print(file.read())

# print(file.readlines())

# print(file.readline())
# print(file.readline())

# file.close()
# ----------------------------------------

# file = open("newfile.txt", "w")

# # file.write("Hello World\n")

# file.writelines(["Hello World\n", "Hello World\n", "Hello World\n"])

# file.close()

# ----------------------------------------

# file = open("newfile.txt", "a")

# file.write("Hello World\n")

# file.close()

# ---------------------------

# for w+, a+, r+
# f = open("newfile.txt", "w+")

# print("Pointer is at: ", f.tell())

# content = f.read()
# print(content)

# f.write("hello world\n")
# f.write("hello world 2\n")

# f.seek(0)

# content = f.read()
# print(content)

# ------------------------------

# import time
# f = open("new_file_1.txt", "w")

# for i in range(1, 61):
#     print("write line ", i)
#     f.write("line " + str(i) + "\n")
#     if (i % 10 == 0):
#         f.flush()
#     time.sleep(1)

# f.close()

# ----------------------------------

# import os

# cwd = os.getcwd()
# print(cwd)

# cw_dir_and_files = os.listdir()
# print(cw_dir_and_files)

# path = os.path.join("..", "test.txt")
# f = open(path, "w")
# f.write("Hello World\n")

# ----------------------------

import os
print()

path = os.path.join(os.getcwd(), "..")
print(path)
parent_dir =  os.path.abspath(path)
print(parent_dir)
print("List Dir: ", os.listdir(parent_dir))

print()