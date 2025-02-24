
fname = input('Enter A File Name: ')
try:
    fhand = open(fname)
except:
    print("File can not be opened:",fname)
    quit()

for line in fhand:
    line  = line.rstrip()
    print(line.upper())
