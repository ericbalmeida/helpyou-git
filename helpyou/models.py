from django.db import models

class TD_Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Mensagens(models.Model):
    mensagem = models.TextField(null=True, blank= True)

    def __str__(self):
        return ''
