# Recursive Function
def show(n):
    if n == 0:
        return  # this is called Control Return
    print(n)
    show(n-1)
    print("END")

show(5)