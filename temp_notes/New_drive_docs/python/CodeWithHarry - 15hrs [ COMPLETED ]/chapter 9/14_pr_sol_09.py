# file1 = "copy.txt"
file1 = "log.txt"
file2 = "this.txt"

with open(file1, "r") as f:
    f1 = f.read()

with open(file2, "r") as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")