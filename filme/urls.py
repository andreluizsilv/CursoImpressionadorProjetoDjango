from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhefilmes, PesquisaFilmes

app_name='filme'

urlpatterns = [
     path('', Homepage.as_view(), name='homepage'),
     path('filmes/', Homefilmes.as_view(), name='homefilmes'),
     path('filmes/<int:pk>', Detalhefilmes.as_view(), name='detalhesfilmes'),
     path('pesquisa/', PesquisaFilmes.as_view(), name='pesquisafilmes'),
]
