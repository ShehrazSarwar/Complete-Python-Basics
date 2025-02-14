#Loops in python

#While Loop (definite loop)
n = 5
while n > 0:
    print(n)
    n = n - 1   #here n is decrementing so that's why it's a definite loop
print("Done with while loop!")

#There is no do-while loop in python
#,but we can use While True to make a loop infinite and then break it using break

while True:
    line = input(">").lower()   #lower() converts each character to lower case
    if line == "done":
        break
    print(line)
print("Done!")

#continue skips the current iteration and starts the next one
#,skip the code which is below continue and start the next iteration

while True:
    line = input(">").lower()
    if line[0] == '#':   #checking if first character is '#' then skip that iteration
        continue
    if line == "done":
        break
    print(line)
print("Done!")