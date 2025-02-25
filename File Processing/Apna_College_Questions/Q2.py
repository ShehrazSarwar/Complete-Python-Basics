with open('numbers.txt') as f:
    data = f.read()

List = data.split(',')
count = 0
for number in List:
    if int(number) % 2 == 0:
        print(number)
        count += 1

print(f'There are {count} even numbers in the file!')