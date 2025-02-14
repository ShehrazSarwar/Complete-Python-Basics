# Program to find the HCF or GCD of two numbers

n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))

GCD = None
for i in range(1,min(n1,n2)+1):
    if n1 % i == 0 and n2 % i ==0:
        GCD = i

print("GCD is:",GCD)
# min(n1,n2) function to find min between two numbers or more numbers (or a list)
# max(n1,n2) same but find max
# sum() only to calculate the sum of numbers in a collection like list, tuples etc

# Alternative Method, Using an if-else
# if n1<n2:
#     mn = n1
# else:
#     mn = n2



