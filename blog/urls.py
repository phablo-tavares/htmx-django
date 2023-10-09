from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('api/pessoas', views.PessoaList.as_view()),
    path('api/pessoas/<int:pk>', views.PessoaDetail.as_view()),
    path('api/pessoas/create', views.PessoaCreate.as_view()),
    path('api/pessoas/<int:pk>/update', views.PessoaUpdate.as_view()),
    path('api/pessoas/<int:pk>/delete', views.PessoaDelete.as_view()),

    path('formPessoas', views.formPessoas),
    path('formAtualizarPessoa/<int:pk>', views.formAtualizarPessoa),

    path('adicionar-pessoa', views.salvarPessoa, name='adicionar-pessoa'),
    path('atualizar-pessoa', views.salvarPessoa, name='atualizar-pessoa'),
    path('deletar-pessoa/<int:pk>', views.deletarPessoa, name='deletar-pessoa'),

    path('filtrar-dados-tabela', views.filtrarDadosTabela),

    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
