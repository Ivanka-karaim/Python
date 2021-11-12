import random
import os
import timeit
# file = open("files.txt", "w")
# while os.path.getsize("files.txt") <= 50000000:
#     file.write(str(random.randint(1, 1000)) + "\n")
# print(os.path.getsize("files.txt"))
# file.close()
s = """
with open("files.txt", "r") as file:
    x = file.readlines()
    res = 0
    for i in x:
        if i.strip().isdigit():
            res += int(i.strip())
"""
print(timeit.timeit(s, number=10))
s = """
with open("files.txt", 'r') as file:
    res = 0
    for line in file:
        if line.strip().isdigit():
            res += int(line.strip())
"""
print(timeit.timeit(s, number=10))
s = """
with open("files.txt",'r') as file:
    x = (int(line.strip()) for line in file if line.strip().isdigit())
    res = sum(x)
"""
print(timeit.timeit(s, number=10))
