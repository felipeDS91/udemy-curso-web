def calcula_dobro(numero):
	total = numero * 2
	return total

a = calcula_dobro(8)
print(a)


# As an array as a parameter
def calcula_soma_numeros(*numeros):
	total = 0
	for numero in numeros:
		total += numero
	return total
	# or just return sum(numeros) 

soma = calcula_soma_numeros(2,3,4,6)
print("O resultado da soma e ", soma)


# As an array as a parameter with 2 dimensions
def calcula_soma_numeros2(num1, num2,**numeros):
	resultado = 0
	for item in numeros:
		resultado =+ numeros[item]
	return resultado 
	# Or Return sum(numeros.values())

soma2 = calcula_soma_numeros2(num1=5, num2=10, num3=20)
print("O resultado da soma da funcao2 e ", soma2)