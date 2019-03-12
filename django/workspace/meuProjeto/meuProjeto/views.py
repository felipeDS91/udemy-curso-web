from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola Mundo')

def clientes(resquest):
    return HttpResponse('Maria, Jose, Joao')