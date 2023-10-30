from django.db import models

# Create your models here.
from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    link_imagem = models.URLField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    

class Conexao(models.Model):
    conexaoA = models.ForeignKey(Ator, on_delete=models.CASCADE, related_name='conexoes_a')
    conexaoB = models.ForeignKey(Ator, on_delete=models.CASCADE, related_name='conexoes_b')

    def __str__(self):
        return f"{self.conexaoA.nome} <-> {self.conexaoB.nome}"