from django.db import models
from datetime import date


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    dataDeNascimento = models.DateField()

    @property
    def idade(self):
        hoje = date.today()
        anos = hoje.year - self.dataDeNascimento.year - \
            ((hoje.month, hoje.day) <
             (self.dataDeNascimento.month, self.dataDeNascimento.day))
        if anos < 0:
            anos = 0
        return anos

    def __str__(self):
        return self.nome
