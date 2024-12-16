from django.db import models
# from django.utils.timezone import now

class Contact(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
