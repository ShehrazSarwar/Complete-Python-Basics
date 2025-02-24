# To search from a file

# fhand = open('Test.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# We need to tackle print() function's newline character using rstrip()
# To fix this issue we need to strip each line from right using rstrip()
# To output the file without read() correctly!
# Note: newline treated as a whitespace

# fhand = open('Test.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# Alternate method using continue:
fhand = open('Test.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)