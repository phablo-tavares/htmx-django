from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework import status
from .util import getAllInstances, getSingleInstance, createInstance, updateInstance, deleteInstance
from blog.forms import PessoaForm
from django.http import HttpResponse


class PessoaList(APIView):

    def get(self, request):
        response = getAllInstances(
            model=Pessoa, serializerClass=PessoaSerializer)
        return response


class PessoaDetail(APIView):

    def get(self, request, pk):
        response = getSingleInstance(
            model=Pessoa, serializerClass=PessoaSerializer, pk=pk)
        return response


class PessoaCreate(APIView):

    def post(self, request):
        response = createInstance(
            model=Pessoa, serializerClass=PessoaSerializer, data=request.data)
        return response


class PessoaUpdate(APIView):

    def put(self, request, pk):
        response = updateInstance(
            model=Pessoa, serializerClass=PessoaSerializer, pk=pk, data=request.data)
        return response


class PessoaDelete(APIView):

    def delete(self, request, pk):
        response = deleteInstance(
            model=Pessoa, serializerClass=PessoaSerializer, pk=pk)
        return response


def formPessoas(request):
    form = PessoaForm()
    pessoas = Pessoa.objects.all()
    context = {
        'form': form,
        'pessoas': pessoas,
    }
    return render(request, 'index.html', context)


def formAtualizarPessoa(request, pk):
    pessoa = Pessoa.objects.get(id=pk)
    form = PessoaForm(initial={
        'nome': pessoa.nome,
        'cpf': pessoa.cpf,
        'dataDeNascimento': pessoa.dataDeNascimento,
    })
    context = {
        'form': form,
        'idPessoa': pessoa.id,
    }
    return render(request, 'partials/form-atualizar-pessoa.html', context)


def salvarPessoa(request):
    data = request.POST
    if 'id' in request.POST:
        pessoa = Pessoa.objects.get(id=int(request.POST['id']))
        form = PessoaForm(data or None, instance=pessoa)
    else:
        form = PessoaForm(data or None)
    if form.is_valid():
        pessoa = form.save()
        context = {
            'pessoa': pessoa
        }
        return render(request, 'partials/table-row.html', context)
    pass


def deletarPessoa(request, pk):
    if Pessoa.objects.filter(id=pk).exists():
        Pessoa.objects.get(id=pk).delete()
        return HttpResponse(status=status.HTTP_200_OK)
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
