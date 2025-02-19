num = int(input('Enter number: '))
if num  & 1:  #bitwise AND (&) is faster than %
    print("odd")
else:
    print("even")
