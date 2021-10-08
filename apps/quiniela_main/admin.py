from django.contrib import admin
from apps.quiniela_main.models import Partido, PartidoPleno15, Jugada

# Register your models here.
admin.site.register(Partido)
admin.site.register(PartidoPleno15)
admin.site.register(Jugada)
