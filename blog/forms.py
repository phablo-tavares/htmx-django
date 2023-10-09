from django import forms
from blog.models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'cpf',
            'dataDeNascimento',
        )
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'cpf': forms.NumberInput(attrs={'class': "form-control", 'min': '1', 'step': '1'}),
            'dataDeNascimento': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
        }
