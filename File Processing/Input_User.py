# To input file name from the user and perfrom search operation on it

# fname = input('Enter File Name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count += 1
#         print(line)
#
# print("There are",count,"subject lines in",fname)

# To handle wrong file name (we need to implement try and except)
fname = input('Enter File Name: ')
try:
    fhand = open(fname)
except:
    print("File can't be opened!", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
        print(line.rstrip())  #to handle newline character

print("There are", count, "subject lines in", fname)
