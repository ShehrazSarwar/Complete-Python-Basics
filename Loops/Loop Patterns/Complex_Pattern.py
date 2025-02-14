#Program to print the Complex Pattern With Spaces

try:
    n = int(input("Enter n for loop: "))
except ValueError:
    print("Invalid input!")
    quit()

for i in range(n):
    for j in range(n-int((n/2)+1)-i):
        print("     ",end="")
    if i < int(n/2):
        for j in range(i+1):
            print("*    ",end="")
    else:
        for j in range(n-i):
            print("*    ",end="")
    print()