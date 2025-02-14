#Program to calculate the average of list using loop

the_sum = 0
count = 0
print("Before:",count,the_sum)

for i in [1,2,3,4,5,6,7,8,9,10]:
    the_sum = the_sum + i
    count = count + 1
    print(count,the_sum,i)

print("After Loop:",count,the_sum,"\nAverage:",the_sum/count)