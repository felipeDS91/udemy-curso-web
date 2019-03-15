import re

a = re.match('Pr', 'Programe facil')
a = re.match('[pP]y', 'Pyton')
a = re.match('[a-zA-Z]y', 'Python')
a = re.findall('[a-zA-Z]y', 'Python jython Programe facil')
a = re.findall('[a-zA-Z][a-zA-Z]', 'Python jython 10')
a = re.findall('[a-zA-Z][a-zA-Z]+', 'Python jython')
a = re.findall('\w+', 'Python jython')

print(a)

# Use this regex to separate URL on our file "urls.py"
end = 'www.site.com/clientes/17856'
print(re.search(r'clientes/\d+$', end))

print(re.split(r'clientes/(?P<id>\d+)', end))