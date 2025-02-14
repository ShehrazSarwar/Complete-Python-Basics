# Program to find the factorial of two numbers and divide both

def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact

n1 = int(input('Enter 1st Number: '))
n2 = int(input('Enter 2nd Number: '))

fact_1 = factorial(n1)
fact_2 = factorial(n2)

Cal_Division = fact_1 / fact_2
print(f"Factorial Division Of Both: {Cal_Division}")
