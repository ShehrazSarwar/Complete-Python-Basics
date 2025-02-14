# Q)Gross pay with if-else and try except

try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate per hour: "))

except ValueError:
    print("Please enter a valid integer!")
    quit()

if hours > 40:
    overtime = hours - 40
    pay = (overtime * 1.5 * rate) + (40 * rate)
    print("The pay is:",pay)
else:
    pay = hours * rate
    print("The pay is:", pay)

