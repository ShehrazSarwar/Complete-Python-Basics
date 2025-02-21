# collection = set() To declare an empty set

collection = {1,2,3,4}
print(collection)

print(type(collection))

# to add an element
collection.add(5)
print(collection)

# Excludes the duplicate elements because sets only include unique elements
collection = {1,2,3,3,4}
print(collection)

collection.add(4)
print(collection)

# to remove the element
collection.remove(2)
print(collection)

# Union
collection2 = {5,6,7,8,1,3}
collection3 = collection.union(collection2)
print(collection3)

# Intersection
collection3 = collection.intersection(collection2)
print(collection3)

# no index required, it removes randomly
collection2.pop()
print(collection2)

# to clear the whole set
collection3.clear()
print(collection3)

# to copy one to another
collection3 = collection.copy()
print(collection3)

collection3 = {2,3,1,5}
collection2 = {3,1,5}

# difference same like maths set
collection4 = collection3.difference(collection2)
print(collection4)

# to add one set values to another
collection4.update(collection2)
print(collection4)
print(len(collection4))