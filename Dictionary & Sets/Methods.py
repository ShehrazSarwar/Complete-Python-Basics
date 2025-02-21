
file_counts = {"JPG":10,"PDF":5,"PY":62,"TXT":10}
print(dir(file_counts))

del file_counts["TXT"]
print(file_counts)

file_counts.pop("PDF")
print(file_counts)

# Returns the dictionary as a list of tuples
# We need to do this when itrating over a dictionary
print(file_counts.items())  #Import method!

print(file_counts.keys()) # Return keys
print(file_counts.values()) # Return Values
# We can also iterate over only keys or values using above funtions

# there are others methods used for iteration over specific values or keys or all
# check iteration file for them

#Dictionary with multiple values (use list for it)
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
#Upate function append new keys and overwrite existing ones values with new
wardrobe.update(new_items)
print(wardrobe)

# Check Google_Questions --> Quizz_Q2.py for Dictionary[Key].append(value)
# append function adds a new value in to the list

print(file_counts.get("PY")) #.get() returns the specified key's value
