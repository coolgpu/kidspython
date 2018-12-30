from pathlib import Path

filename = "file1.txt"
mode = 'r'
# Case 1
print("Case 1:")
f = open(filename, mode) # r for read, w for write, a for append, b for binary
# f.read() will read and return the whole contents of the file.
data = f.read()
print(data)
# If the end of the file has been reached, f.read() will return an empty string ('').
data1 = f.read()
print(data1)
f.close()

# using with open() as ..., the system will automatically close the file
# after the scope of "with" is over
print('Case "with:"')
with open(filename, mode) as f:
    data1 = f.read()
    print(data1)

print("Case 2:")
with open(filename, mode) as f:
    # f.read(n) will read n characters (if text file) or n bytes
    # (if binary file). After reading,
    # the "current position" will move to the next character for further reading
    data = f.read(6)
    print("Type of data from f.read() is {}".format(type(data)))
    print(len(data))
    print(data)
    # read() will resume reading and read the rest part
    datarest = f.read()
    print(len(datarest))
    print(datarest)


# -------- Case 3
print("Case 3:")
with open(filename, mode) as f:
    # f.readline reads 1 line
    data = f.readline()
    print("Type of data from f.readline() is {}".format(type(data)))
    print(data)
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)

# -------- Case 3
print("Case 3.5:")
with open(filename, mode) as f:
    # f.readlines() will reads until EOF using readline()
    # and returns a list containing the lines
    data = f.readlines()
    print("Type of data from f.readlines() is {}".format(type(data)))
    print(data)



# -------- Case 4
print("Case 4:")
with open(filename, mode) as f:
# f.read(n) will read n charactors (if text file) or n bytes (if binary file). After reading,
# the next charactor will be marked as the next one to read
    for line in f:
        print(line)

print("Case 5: open a file for writing")
outfilename = "outfile.txt"
with open(outfilename, 'w') as fout:
    fout.write("This is a newly created file.The following \
    lines will be copied from the input file.\n")
    with open(filename, mode) as fin:
    # f.read(n) will read n charactors (if text file) or n bytes (if binary file).
    # After reading, the next charactor will be marked as the next one to read
        for line in fin:
            fout.write(line)

print("Case 6: open a existing file with mode 'w' will overwrite it")
outfilename = "outfile.txt"
my_file = Path(outfilename)
if my_file.exists() and my_file.is_file():
    print("Warning: {} already exists. Opening it with mode \
    'w' will overwrite it!".format(outfilename))
with open("outfile.txt", 'w') as fout:
    fout.write("{} already exists. It was opened with mode of 'w', \
    thus is overwritten. The following lines will be copied from the input file.\n".format(outfilename))
    with open(filename, mode) as fin:
        for line in fin:
            fout.write(line)

print("Case 7: open a existing file with mode 'a' will append at the end of it")
outfilename = "outfile.txt"
my_file = Path(outfilename)
if my_file.exists() and my_file.is_file():
    print("Warning: {} already exists. Opening it with mode \
    'a' will append at the end!".format(outfilename))
with open("outfile.txt", 'a') as fout:
    fout.write("\n{} already exists. opening with mode of 'a' will append at the end. \
    The following lines will be copied from the input file.\n".format(outfilename))
    with open(filename, mode) as fin:
        for line in fin:
            fout.write(line)




