from rest_framework import generics

from apps.quiniela_main.models import Jornada, Partido, PartidoPleno15, Jugada
from apps.quiniela_main.api.serializers import JornadaSerializer, PartidoSerializer, PartidoPleno15Serializer, JugadaSerializer


class JornadaListAPIView(generics.ListAPIView):
    serializer_class = JornadaSerializer

    def get_queryset(self):
        return Jornada.objects.all()


class PartidoListAPIView(generics.ListAPIView):
    serializer_class = PartidoSerializer

    def get_queryset(self):
        return Partido.objects.all()


class PartidoPleno15ListAPIView(generics.ListAPIView):
    serializer_class = PartidoPleno15Serializer

    def get_queryset(self):
        return PartidoPleno15.objects.all()


class JugadaListAPIView(generics.ListAPIView):
    serializer_class = JugadaSerializer

    def get_queryset(self):
        return Jugada.objects.all()
