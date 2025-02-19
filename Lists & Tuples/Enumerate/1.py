def skip_elements(elements):
	even_elements = []
	for index, even in enumerate(elements):
		if index % 2 == 0:
			# print(index)
			even_elements.append(even)
	return even_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']