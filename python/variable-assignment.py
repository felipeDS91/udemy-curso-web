a = 10

maisIgual, menosIgual, vezesIgual, divididoIgual, moduloIgual = 9,9,9,9,9

# str() = cast to string
print(str(menosIgual) + '-' + str(vezesIgual))

maisIgual += 1  # resultado 10
menosIgual -= 1 # resultado 8
vezesIgual *= 1 # resultado 9
divididoIgual /= 1 # resultado 9
moduloIgual %= 2 # resultado 1

a, b, c = 2,4,8

# Here we can pass to many variables, many values in the same time separeted by ","
a, b, c = a*2, a+b+c, a*b*c