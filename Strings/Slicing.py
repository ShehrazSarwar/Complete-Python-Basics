
# Slicing String
# We can access Characters in a string in different ways using indexing
s = 'Monty Python'   #Starts from index 0
print(s)
print(s[0:4])   #from 0 to 3-1
print(s[6:20])  #in this case there is no Traceback

print(s[:2])  #from start to 2-1
print(s[6:])  #from 6 to last
print(s[:]) #whole string

# Negative Slicing
print(s[-6:len(s)]) #from P to length of string final position - 1 or 12
print(s[-12:-7])

# Slices with a step interval
#string[start:stop:step]
text = "Hello, World!"
print(text[::2])   # Output: 'Hlo ol!' (every second character)
print(text[::-1])  # Output: '!dlroW ,olleH' (reversed string)
