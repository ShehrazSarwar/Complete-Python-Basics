# Split function for String

name = "Sheeraz Sarwar"

# Check if there is a space or any other character in a string from we want to split
if " " in name:
    names = name.split(" ") #split the string from " " (space)
    # Now names is a list having two different strings
    print(names)

# Use case Of split()

# Converts string input (even fractions means 4/5 etc.) to float
def frac_string(in_string):
    if "/" in in_string:
        numbers = in_string.split("/")
        try:
            n = float(numbers[0])
            d = float(numbers[1])
            ans = n / d
            return ans
        except ValueError:
            print("Invalid input!")
            quit()
    else:
        try:
            ans = float(in_string)
            return ans
        except ValueError:
            print("Invalid input!")
            quit()

number = input("Enter Number In Fraction: ")
print("In Fraction:",frac_string(number))
