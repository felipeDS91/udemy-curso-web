from django.shortcuts import render
from django.http import HttpResponse

def clientes(resquest):
    return HttpResponse('Maria, Jose, Joao')

def cliente_detalhe(request, id):
    return HttpResponse('Cliente detalhe ' + str(id))

def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s seja bem vinda' % nome)
