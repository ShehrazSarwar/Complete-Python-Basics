
print("keys() and values() return lists")
file_counts = {"JPG":10,"PDF":5,"PNG":5,"TXT":15}
print(file_counts.keys())
print(file_counts.values())

print("\nIterate over keys only!")
file_counts.values()
for extention in file_counts: #or for extention in file_counts.keys():
    print(extention)

print("\nIterate over values only!")
for value in file_counts.values():
    print(value)

print("\nIterate completely!")
for files in file_counts.items():  #returns tuples
    print(files)

print("\nIterate completely with proper formating!")
for ext, amount in file_counts.items():  #need to use two variables as .items() returns tuples
  print("There are {} files with the .{} extension".format(amount, ext))

