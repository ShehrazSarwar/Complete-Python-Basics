fhand = open('Test2.txt', 'w')  # overwrites the entire file
fhand.write('This is only for testing writing mode!')

fhand.close()

fhand = open('Test2.txt', 'a')  # add new line at the end of a file
fhand.write('\nThis is only for testing append mode!')

fhand.close()

fhand = open('Test2.txt')
# data = fhand.read()  # reads the entire file and stored it into a single variable
# print(data)

data = fhand.readline()  # reads only 1 line at a time
print(data)

fhand.close()