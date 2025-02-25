with open('practice.txt') as f:
    data = f.read()

data = data.replace('Java', 'Python')
print(data)

with open('practice.txt', 'w') as f:
    f.write(data)

print("Java replaced with Python!")

