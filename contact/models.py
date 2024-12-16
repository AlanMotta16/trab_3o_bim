from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    mensagem = models.TextField()
    data_recebimento = models.DateTimeField(default=now, editable=False)
    resposta = models.TextField(blank=True, null=True)
    data_resposta = models.DateTimeField(blank=True, null=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
