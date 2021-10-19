from rest_framework import generics

from apps.quiniela_main.models import Jornada, Partido, PartidoPleno15, Jugada
from apps.quiniela_main.api.serializers import JornadaSerializer, PartidoSerializer, PartidoPleno15Serializer, JugadaSerializer


class JornadaListApi(generics.ListAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer


class PartidoListApi(generics.ListAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer


class PartidoPleno15ListApi(generics.ListAPIView):
    queryset = PartidoPleno15.objects.all()
    serializer_class = PartidoPleno15Serializer


class JugadaListApi(generics.ListAPIView):
    queryset = Jugada.objects.all()
    serializer_class = JugadaSerializer
