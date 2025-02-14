#Q)5.1 Program (PY4E)

the_sum = 0
the_count = 0

while True:
    number = input("Enter a number: ").lower()
    if number == "done":
        break
    try:
        number = int(number)
    except ValueError:
        print("Invalid input")
        continue
    the_sum = the_sum + number
    the_count = the_count + 1

#Print result
print(the_sum,the_count,the_sum / the_count)
