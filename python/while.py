condicao = True
while condicao:
	print('Executou')
	condicao = False
else:
	print('Fim do loop')

i = 0
while i < 10:
	# Not print number 5
	if i == 5:
		i = i + 1
		continue
	# If "i" equals 8 stop and out
	if i == 8:
		break
	print(i)
	i = i + 1
else:
	print('Fim do loop')