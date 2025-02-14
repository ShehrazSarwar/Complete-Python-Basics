#Program to calculate the sum of list through a loop

the_sum = 0
print("Sum before:",the_sum)

for i in [1,2,3,4,5,6,7,8,9,10]:
    the_sum = the_sum + i
    print(the_sum,i)

print("Sum after loop:",the_sum)