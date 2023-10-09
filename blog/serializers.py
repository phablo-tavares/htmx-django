from . import models
from rest_framework import serializers


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = [
            'id',
            'nome',
            'cpf',
            'dataDeNascimento',
            'idade',
        ]
