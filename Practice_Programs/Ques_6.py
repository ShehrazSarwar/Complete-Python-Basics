# Program to calculate the sum of a multiplication table

number = int(input('Enter number: '))

Sum = 0

for i in range(1,11):
    Sum += number*i

print(f"The Sum Of A Table Of {number} is {Sum}")