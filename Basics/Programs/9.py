#Program to search something in a for loop using boolean variable

found = False
print("Before:",found)

for value in [2,41,4,51,33,75,3,25]:
    if value == 3:
        found = True
        print(found, value)
        break

print("After Loop:",found)