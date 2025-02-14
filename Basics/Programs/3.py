# Q)Gross pay with if-else to calculate 1.5 times for hours above 40

hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours > 40:
    overtime_hours = hours - 40
    pay = (overtime_hours * 1.5 * rate) + (40 * rate)
    print("The pay is: ", pay)
else:
    pay = hours * rate
    print("The pay is: ", pay)
