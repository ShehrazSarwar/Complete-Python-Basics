# we can use 'with' in order to avoid file.close()

with open('Test2.txt') as f:
    data = f.read()
    print(data)