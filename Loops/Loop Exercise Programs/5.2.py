#Q)5.2 Program (PY4E)

largest = None
smallest = None

while True:
    number = input("Enter a number: ").lower()
    if number == "done":
        break
    try:
        number = int(number)
    except ValueError:
        print("Invalid input")
        continue
    if largest is None and smallest is None:
        largest = number
        smallest = number
    elif number < smallest:
        smallest = number
    else:
        largest = number

#Print result
print("Smallest:",smallest,"\nLargest:",largest)
