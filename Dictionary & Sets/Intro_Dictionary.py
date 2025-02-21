# Intro To Dictionary!
# Dictionaries are mutable, meaning they can be modified by adding, removing,
# and replacing elements in a dictionary, similar to lists.

x = {}
print(type(x))

file_counts = {"JPG":10,"PDF":5,"PY":62}
print(file_counts)

# To print the specified value
print(file_counts["PDF"])
file_counts["TXT"] = 10 #or any integer also works file_counts[10] = "TXT"
print(file_counts)

# We can't print through index
# print(file_counts[0]) will generate the error

print("PDF" in file_counts)
print("html" in file_counts)

del file_counts["TXT"]
print(file_counts)

file_counts.pop("PDF")
print(file_counts)