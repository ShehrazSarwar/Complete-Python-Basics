#gross-pay simple short input and output program
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)  #converting type string to type float
print("Pay:",pay)  #here comma(,) will add space by default
#print("Pay "+ str(pay)) this is same thing but this time it's converting type float to string and then concatinate it
print(type(pay)) #print type of pay


#just for logic behind string input
x = input("Enter Integer: ")
x = int(x)
print(type(x))

