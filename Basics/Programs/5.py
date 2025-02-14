#Program to find the largest number in a loop and store it in a variable

largestSoFar = -1
print("Before loop largest is",largestSoFar)
for num in [2,41,4,51,33,75,3,25]:
    if num > largestSoFar:
        largestSoFar = num
    print(largestSoFar,num)
print("After loop largest number is now",largestSoFar)

