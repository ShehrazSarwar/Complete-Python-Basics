#Correct way to find the largest or smallest number using a loop

the_Smallest = None
#Here None is something like null in python which means there is no value assigned,yet
#We compare None,True and False using is and is not operators, 'is' is like '==' but stronger
print("Before:",the_Smallest)

for value in [9,41,4,51,33,75,3,25]:
    if the_Smallest is None:
        the_Smallest = value
    elif value < the_Smallest:
        the_Smallest = value
    print(the_Smallest,value)

print("After Loop:",the_Smallest)