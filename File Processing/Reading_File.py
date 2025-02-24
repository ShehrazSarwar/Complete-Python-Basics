# Reading the whole file using read() function
# we can read the whole file (newlines and all) into a single string

fhand = open('Test.txt')
inp = fhand.read()
print("Total Characters:",len(inp))

print(inp[:20]) #prints first 20 characters from the string
print("\nWhole File:")
print(inp)