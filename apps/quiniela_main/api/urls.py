from django.urls import path
from apps.quiniela_main.api.api import JornadaListAPIView, PartidoListAPIView, PartidoPleno15ListAPIView, JugadaListAPIView

urlpatterns = [
    path('jornadas/', JornadaListAPIView.as_view(), name='jornada_api'),
    path('partidos/', PartidoListAPIView.as_view(), name='partido_api'),
    path('partidos-pleno15/', PartidoPleno15ListAPIView.as_view(), name='partidopleno15_api'),
    path('jugadas/', JugadaListAPIView.as_view(), name='jugada_api'),
]
