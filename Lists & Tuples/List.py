# Here is lists in python that can store mulitple data types within the single variable
# Lists are mutable means we can repalce it through indexes

fruits = ["apple","orange","banana","apple","coconut"]
print(fruits)

# print("apple" in fruits)  #check if apple is in the list or not (return boolean)
if "apple" in fruits:
    print("Apple Found!")

# We can iterate over a list using for loop
print("\nPrint using for loop")
for fruit in fruits:
    print(fruit)

print("\nPrint fruits except apples without modifying the list")
for fruit in fruits:
    if fruit != "apple":
        print(fruit)

# print("\nLenght of fruits list is",len(fruits)) Or Using f string
print(f"\nLength of fruits list is {len(fruits)}")
print(type(fruits))

# Slicing are also possible same as strings (pos and neg both)
print()
print(fruits[:3])
print(fruits[-4:-1])
print(fruits[-5:])
print()
# To print in reverse order using slicing with steps list[start:stop:step]
print(fruits[::-1])
print(fruits[::2])  # (every second fruit)
print()

print(fruits[2]) #directly print through index
fruits[0] = "pineapple" #since lists are mutable we can replace values
# print(fruits[5]) or fruits[5] = "mango" -> Error index out of bound or range
print(fruits)

# Lists concatination
fruits_count = [1,2,3,4,5,"fruits"]  # Can store multiple data types
new_fruits = fruits + fruits_count
print(new_fruits)


