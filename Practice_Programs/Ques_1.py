
# Program to calculate the sum of square of first n integers entered by the user.

n = int(input('Enter number (n): '))
Sum = 0

for i in range(1,n+1):
    Sum = Sum + (i*i)

print("The Sum Of Square Of N Integers Is:",Sum)

