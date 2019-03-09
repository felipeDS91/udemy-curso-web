# For with range of numbers
for i in range(4, 10):
	print(i)
else:
	print('Fim loop')

# For with a string
for i in 'iteracao':
	print(i)
else:
	print('Fim loop')	

# For with an array
for i in ['item 1', 'item 2', 'item 3']:
	print(i)
else:
	print('Fim loop')

# For with two arrays in same time
list1 = ['Apple', 'Banana', 'Melon']
list2 = ['Tomato', 'Onion', 'Carrot']
for i, j in zip(list1, list2):
	print(i, j)

# For with "enumerate" can get the index of a list on your first parameter
for i, j in enumerate(list1):
	print (i, j)