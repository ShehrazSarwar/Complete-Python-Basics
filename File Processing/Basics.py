# let's learn about file input and output
# To open a file use open('file') function (by default it is set to read mode) --> open('file','r')
# To open a file in write mode open('file','w')
# open() returns a "file handle" - a variable used to perform operations on the file

fhand = open('Test.txt')  #Traceback if the file doesn't exist!
# print(fhand)  #prints out file name and mode

# Note: A text file has newlines at the end of each line (\n)
# A file handle can be treated as a sequence of strings

# for line in fhand:
    # print(line)

# Countring lines in a file:
count = 0
for line in fhand:
    count += 1
print("Line Count:",count)

