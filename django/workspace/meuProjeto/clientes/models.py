from django.db import models
# Fields for models
# https://docs.djangoproject.com/pt-br/2.1/ref/models/fields/
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=True, null=False)
