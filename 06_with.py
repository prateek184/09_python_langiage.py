f = open("file.txt")
print(f.read())
f.close()
# the same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# you do not have to explicitly close the file