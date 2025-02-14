# Tuples is a collection in python like lists but these are immutable
# we can not manipulate Tuples (immutable)
# we can store multiple data types like lists

fruits = ("apple","orange","banana","coconut")
print(fruits)

fruits = ("apple")  #we didn't manipulate here we create new list using the existing variable
print(fruits)

# in tuple if we store single element, python will not consider it as a tuple then!
print(type(fruits))

fruits = ("apple",) # using comma with single element to make it a tuple
print(type(fruits))

fruits = ("apple","orange","banana","coconut")

# Let's check the methods of tuples
# print(dir(fruits))

print(fruits.index("banana"))
print(fruits.count("orange"))

# other methods which works for both lists and tuples (for all collections)

print(max(fruits))  #print the largest element in a collection, work good on numbers
print(min(fruits))  #print the smallest element in a collection, work good on numbers

numbers = (1,2,3,4,5)
print(sum(numbers))  #to calculate the sum
print(sorted(numbers)) #return's a sorted list

# we can manipulate the tuples by first converting it to lists and then back to tuple
numbers = list(numbers)
numbers.append(6)
numbers.sort(reverse = True)
numbers = tuple(numbers)
print(numbers)

# we can concatinate the tuple, but we have to store it in another tuple
new = numbers + fruits
print(new)