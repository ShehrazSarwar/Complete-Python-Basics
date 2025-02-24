fname = input('Enter a file name: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)
many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w,0) + 1

print(many)

# Find the word with the largest count:
largest = None
bigWord = None
for key,value in many.items():
    if largest is None or value > largest:
        largest = value
        bigWord = key

print(bigWord, largest)