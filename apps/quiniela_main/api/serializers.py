from rest_framework import serializers
from apps.quiniela_main.models import Partido, PartidoPleno15, Jugada


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido


class PartidoPleno15Serializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoPleno15


class JugadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugada

