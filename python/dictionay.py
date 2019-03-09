d = {'nome':'fulado', 'idade':18}

print(d['nome'])

# Show all possible commands
#print(dir(d))

d.fromkeys([1,2,3], 'x')
print(d)

dict.fromkeys([1,2,3], 'x')


for i in d:
	print(i)

for i in d.items():
	print(i)