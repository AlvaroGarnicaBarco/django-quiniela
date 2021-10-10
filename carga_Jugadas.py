import os
import django
from apps.quiniela_main.models import Jornada, Jugada
from apps.quiniela_main.config import jornada_actual
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiniela_old.settings')
django.setup()


def carga_jugadas():
    df = pd.read_pickle("apps/quiniela_app/df.pkl")

    try:
        jornada = Jornada.objects.get(num_jornada=jornada_actual)
    except:
        return print(f'La jornada {jornada_actual} no existe en el model Jornada')

    lista_jugadas = []
    for index in range(len(df)):
        j = Jugada(
            jornada=jornada,
            combinacion=df['Jugada'].iloc[index].replace(' ', ''),
            pos_est=df['Posición estimada'].iloc[index],
            pos_real=df['Posición real'].iloc[index],
            unos=df['1s'].iloc[index],
            equis=df['Xs'].iloc[index],
            doses=df['2s'].iloc[index],
            mas_probs=df['signos + probables'].iloc[index],
            menos_probs=df['signos - probables'].iloc[index],
            partido_1=df['partido_1'].iloc[index],
            partido_2=df['partido_2'].iloc[index],
            partido_3=df['partido_3'].iloc[index],
            partido_4=df['partido_4'].iloc[index],
            partido_5=df['partido_5'].iloc[index],
            partido_6=df['partido_6'].iloc[index],
            partido_7=df['partido_7'].iloc[index],
            partido_8=df['partido_8'].iloc[index],
            partido_9=df['partido_9'].iloc[index],
            partido_10=df['partido_10'].iloc[index],
            partido_11=df['partido_11'].iloc[index],
            partido_12=df['partido_12'].iloc[index],
            partido_13=df['partido_13'].iloc[index],
            partido_14=df['partido_14'].iloc[index]
        )
        lista_jugadas.append(j)

    Jugada.objects.bulk_create(lista_jugadas)


if __name__ == "__main__":
    print('Por favor espere...')
    carga_jugadas()
