#for loops are definite loops in

#Here i is an iteration variable and in is checking how many times to run according to the list of numbers
#,which are 5,4,3,2,1 here so for loop will execute 5 times and i takes value of list one by one
for i in [5,4,3,2,1]:
    print(i)
print("Done with integer for loop!\n")


#another example of for loop working on list of strings
friends = ["Jack","Tom","Oggy"] #lists can also have multiple data types
for friend in friends:  #here friend is an iteration variable
    print("Happy new year",friend)
print("Done with string for loop!\n")


#print through list index
for i in range(len(friends)):   #starting from zero to length of list(friends)
    print(f"{i+1}: {friends[i]}")
print("Done with print through index loop")