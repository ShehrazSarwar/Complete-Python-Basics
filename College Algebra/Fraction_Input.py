
# Converts string input (even fractions) to float, that means 4/5 etc
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
