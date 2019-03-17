from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

class EmpregadoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos',)
    search_fields = ('id', 'nome', 'departamentos__nome') # "dapartamentos__nome" is searching in relation ManyToMany

admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)

#admin.site.register(Cliente)

# Register your models here.
