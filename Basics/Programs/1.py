#Q)Find if user inputted number is even or odd

number = input("Enter any number: ")
try:
    print("Converting to integer!")
    number = int(number)
    if number % 2 == 0:   #can be written as if (number%2) == 0
        #print("The number is even")
        print(f"The number {number} is even")  #printing through f string
    else:
        #print("The number is odd")
        print("The number",number,"is odd")   #printing through coma (Comma creates the space by default)

except ValueError:
    print("Can't be converted to integer")
    print("Please write decimal number only!")
