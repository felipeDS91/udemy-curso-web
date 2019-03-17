from django.db import models
# Fields for models
# https://docs.djangoproject.com/pt-br/2.1/ref/models/fields/
# Create your models here.

# Example of ManyToMany relation
class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Example of OneToOne relation
class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Empregado(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=True, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento)
    foto = models.ImageField(upload_to='cliente_fotos') # upload to specific folder

    # method that defines the valeu of showing on admistration django
    def __str__(self):
        return self.nome

# Example of OneToMany relation
class Telefone(models.Model):    
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    empregado = models.ForeignKey(Empregado, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao + ' - ' + self.numero
