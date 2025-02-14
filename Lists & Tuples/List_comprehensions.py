
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

squared_numbers = [x ** 2 for x in numbers if x!=3]  # with if
print(squared_numbers)


# Usecase:
sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)

# with list comprehension
# sequence = range(10)
# print(sequence)
# new_list = [x for x in sequence if x % 2 == 0] or
new_list = [x for x in range(10) if x % 2 == 0]
print(new_list)
