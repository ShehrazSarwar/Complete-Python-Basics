# List Methods

fruits = ["apple","orange","banana","coconut"]
print(fruits)

# print(dir(fruits)) # To check all methods
# print(help(fruits)) # to check description of each method

# to add an element in the end of the list
fruits.append("lichi")
print(fruits)

# to remove the first occurance of any element
# fruits.remove("banana")
# print(fruits)

# to remove through index
fruits.pop(2)
print(fruits)

# to insert an element at the specified index of a list
fruits.insert(0,"pineapple")
print(fruits)

# another way to remove an element through index
del fruits[0]
print(fruits)

# to copy list to another list
new_fruits = fruits.copy()
new_fruits.insert(0,"New Fruit List")
print(new_fruits)

# to count the number of specified element
print(fruits.count("orange"))

# to check the index of any element
print(fruits.index("lichi"))
# print(fruits.index("banana") # Error -> banana is not in the list

# to sort the list in ascending order
fruits.sort()
print("Sorted: ",fruits)  # sort first character (alphabet-wise)
numbers = [33,23,22,112,2,1,3]
numbers.sort()
print("Sorted: ",*numbers)   #* to print without [ ]

# to sort the list in descending order
numbers.sort(reverse = True)
print("Sorted Descending: ",numbers)

# to reverse the list
print("Original Fruits List: ",fruits)
fruits.reverse()
print("Reversed: ",fruits)

# there is another method to concatinate the lists (Using extend())
fruits.extend(numbers)
print(fruits)

# to clear the list
fruits.clear()
print(fruits)

# fruits = ["apple","orange","banana","apple","coconut"]
# This approch is not good because it calls the remove funtion multiple times
# 0(n^2) Time Complexity
# apples = fruits.count("apple")
# for i in range(apples):
#     fruits.remove("apple")
# there is a topic in python called List Comprehension which is recommended to remove multiple
# elements from a list