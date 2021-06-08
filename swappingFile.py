import os
import shutil

file1 = "file1.txt"
file2 = "file2.txt"
def swapFileMeanness():
    with open (file1, "r") as a:
        dataA = a.read()
    with open (file2, "r") as b:
        dataB = b.read()
    with open (file1, "w") as a:
        a.write(dataB)
    with open (file2,"w") as b:
        b.write(dataA)
swapFileMeanness()