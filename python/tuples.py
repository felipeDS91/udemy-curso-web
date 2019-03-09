# Tuples = ()
# A Tuple is imutable and spend less space in memory than a list for exemple

a = (1,2,3,'teste', 2, 'teste 2')

print(str(a))

# Show all possibles commands of variable like a auto complete
print(dir(a))

# Show to us a list of possibles commands of a this parameter
print(help(a))

# Find a value on tuple
valueSearch = 2
if a.count(valueSearch) > 0:
	print(a.index(valueSearch))	

for i in a:
	print(i)


