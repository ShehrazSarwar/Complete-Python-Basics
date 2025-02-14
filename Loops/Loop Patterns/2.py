#Pattern 2: Simple Reverse Right Triangle

#Write no of rows here
n = 5

for i in range(n):
    for j in range(i+1):
        print("  ",end="")
    for j in range(n-i):
        print("* ",end="")
    print()