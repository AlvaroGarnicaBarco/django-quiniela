from rest_framework import serializers
from apps.quiniela_main.models import Jornada, Partido, PartidoPleno15, Jugada


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'


class PartidoSerializer(serializers.ModelSerializer):
    jornada = serializers.SlugRelatedField(read_only=True,
                                           slug_field='num_jornada'
                                           )

    class Meta:
        model = Partido
        fields = '__all__'


class PartidoPleno15Serializer(serializers.ModelSerializer):
    jornada = serializers.SlugRelatedField(read_only=True,
                                           slug_field='num_jornada'
                                           )

    class Meta:
        model = PartidoPleno15
        fields = '__all__'


class JugadaSerializer(serializers.ModelSerializer):
    jornada = serializers.SlugRelatedField(read_only=True,
                                           slug_field='num_jornada'
                                           )

    class Meta:
        model = Jugada
        fields = '__all__'
