from django.urls import path
from apps.quiniela_main.api.api import JornadaListApi, PartidoListApi, PartidoPleno15ListApi, JugadaListApi

urlpatterns = [
    path('jornadas/', JornadaListApi.as_view(), name='jornada_api'),
    path('partidos/', PartidoListApi.as_view(), name='partido_api'),
    path('partidos-pleno15/', PartidoPleno15ListApi.as_view(), name='partidopleno15_api'),
    path('jugadas/', JugadaListApi.as_view(), name='jugada_api'),
]

