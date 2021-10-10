import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiniela.settings.local')
django.setup()

import requests
from bs4 import BeautifulSoup
from apps.quiniela_main.models import Jornada, Partido, PartidoPleno15
from apps.quiniela_main.config import jornada_actual


def carga_partidos():
    try:
        jornada = Jornada.objects.get(num_jornada=jornada_actual)
    except:
        return print(f'La jornada {jornada_actual} no existe en el model Jornada')

    respuesta = requests.get('https://www.eduardolosilla.es/')
    soup = BeautifulSoup(respuesta.content, 'html.parser')

    if soup.find('h3',
                 class_='c-boleto-multiples-caja-base-header__container__jornada ng-star-inserted').text.strip().split()[
        -1] != str(jornada_actual):
        print('Jornada que se está intentando generar partidos no corresponde a la jornada actual')

    else:
        base = soup.find(id="body")
        # carga partidos no pleno 15
        partidos = base.find_all('div', class_='c-caja_base__partido u-clearfix ng-star-inserted')

        for idx, partido in enumerate(partidos):
            all_probs = partido.find_all(class_='u-txt-general c-boleto-multiples-porcentajes__row__normal')

            orden_partido = idx + 1
            dia = partido.find(class_='c-marcador-horario__time__day').text.strip()
            hora = partido.find(class_='c-marcador-horario__time__hour').text.strip()
            local = partido.find(class_='c-equipos__teams m-short ng-star-inserted').text.strip().split(' - ')[0]
            visitante = partido.find(class_='c-equipos__teams m-short ng-star-inserted').text.strip().split(' - ')[1]
            prob_real_1 = int(all_probs[6].text.strip())
            prob_real_X = int(all_probs[7].text.strip())
            prob_real_2 = int(all_probs[8].text.strip())
            prob_est_1 = round(int(all_probs[0].text.strip()) * 0.2 + int(all_probs[3].text.strip()) * 0.8)
            prob_est_X = round(int(all_probs[1].text.strip()) * 0.2 + int(all_probs[4].text.strip()) * 0.8)
            prob_est_2 = round(int(all_probs[2].text.strip()) * 0.2 + int(all_probs[5].text.strip()) * 0.8)
            rentabilidad_1 = round(prob_real_1 / prob_est_1, 2)
            rentabilidad_X = round(prob_real_X / prob_est_X, 2)
            rentabilidad_2 = round(prob_real_2 / prob_est_2, 2)

            Partido.objects.update_or_create(
                jornada=jornada,
                orden_partido=orden_partido,
                defaults={
                    'dia': dia,
                    'hora': hora,
                    'local': local,
                    'visitante': visitante,
                    'prob_real_1': prob_real_1,
                    'prob_real_X': prob_real_X,
                    'prob_real_2': prob_real_2,
                    'prob_est_1': prob_est_1,
                    'prob_est_X': prob_est_X,
                    'prob_est_2': prob_est_2,
                    'rentabilidad_1': rentabilidad_1,
                    'rentabilidad_X': rentabilidad_X,
                    'rentabilidad_2': rentabilidad_2
                }
            )

        # carga partido pleno 15
        partido_pleno = base.find(class_='c-caja_base__partido u-clearfix m-pleno15 ng-star-inserted')
        all_probs_pleno = partido_pleno.find_all(class_='u-txt-general c-boleto-multiples-porcentajes__row__pleno')

        dia15 = partido_pleno.find(class_='c-marcador-horario__time__day').text.strip()
        hora15 = partido_pleno.find(class_='c-marcador-horario__time__hour').text.strip()
        local15 = partido_pleno.find(class_='c-equipos__teams ng-star-inserted').text.strip().split('\n')[0]
        visitante15 = partido_pleno.find(class_='c-equipos__teams ng-star-inserted').text.strip().split('\n')[1].strip()
        prob_real_local_0 = int(all_probs_pleno[16].text.strip())
        prob_real_local_1 = int(all_probs_pleno[17].text.strip())
        prob_real_local_2 = int(all_probs_pleno[18].text.strip())
        prob_real_local_M = int(all_probs_pleno[19].text.strip())
        prob_real_visitante_0 = int(all_probs_pleno[20].text.strip())
        prob_real_visitante_1 = int(all_probs_pleno[21].text.strip())
        prob_real_visitante_2 = int(all_probs_pleno[22].text.strip())
        prob_real_visitante_M = int(all_probs_pleno[23].text.strip())
        prob_est_local_0 = round(
            int(all_probs_pleno[0].text.strip()) * 0.2 + int(all_probs_pleno[8].text.strip()) * 0.8)
        prob_est_local_1 = round(
            int(all_probs_pleno[1].text.strip()) * 0.2 + int(all_probs_pleno[9].text.strip()) * 0.8)
        prob_est_local_2 = round(
            int(all_probs_pleno[2].text.strip()) * 0.2 + int(all_probs_pleno[10].text.strip()) * 0.8)
        prob_est_local_M = round(
            int(all_probs_pleno[3].text.strip()) * 0.2 + int(all_probs_pleno[11].text.strip()) * 0.8)
        prob_est_visitante_0 = round(
            int(all_probs_pleno[4].text.strip()) * 0.2 + int(all_probs_pleno[12].text.strip()) * 0.8)
        prob_est_visitante_1 = round(
            int(all_probs_pleno[5].text.strip()) * 0.2 + int(all_probs_pleno[13].text.strip()) * 0.8)
        prob_est_visitante_2 = round(
            int(all_probs_pleno[6].text.strip()) * 0.2 + int(all_probs_pleno[14].text.strip()) * 0.8)
        prob_est_visitante_M = round(
            int(all_probs_pleno[7].text.strip()) * 0.2 + int(all_probs_pleno[15].text.strip()) * 0.8)
        rentabilidad_local_0 = round(prob_real_local_0 / prob_est_local_0, 2)
        rentabilidad_local_1 = round(prob_real_local_1 / prob_est_local_1, 2)
        rentabilidad_local_2 = round(prob_real_local_2 / prob_est_local_2, 2)
        rentabilidad_local_M = round(prob_real_local_M / prob_est_local_M, 2)
        rentabilidad_visitante_0 = round(prob_real_visitante_0 / prob_est_visitante_0, 2)
        rentabilidad_visitante_1 = round(prob_real_visitante_1 / prob_est_visitante_1, 2)
        rentabilidad_visitante_2 = round(prob_real_visitante_2 / prob_est_visitante_2, 2)
        rentabilidad_visitante_M = round(prob_real_visitante_M / prob_est_visitante_M, 2)

        PartidoPleno15.objects.update_or_create(
            jornada=jornada,
            defaults={
                'dia': dia15,
                'hora': hora15,
                'local': local15,
                'visitante': visitante15,
                'prob_real_local_0': prob_real_local_0,
                'prob_real_local_1': prob_real_local_1,
                'prob_real_local_2': prob_real_local_2,
                'prob_real_local_M': prob_real_local_M,
                'prob_real_visitante_0': prob_real_visitante_0,
                'prob_real_visitante_1': prob_real_visitante_1,
                'prob_real_visitante_2': prob_real_visitante_2,
                'prob_real_visitante_M': prob_real_visitante_M,
                'prob_est_local_0': prob_est_local_0,
                'prob_est_local_1': prob_est_local_1,
                'prob_est_local_2': prob_est_local_2,
                'prob_est_local_M': prob_est_local_M,
                'prob_est_visitante_0': prob_est_visitante_0,
                'prob_est_visitante_1': prob_est_visitante_1,
                'prob_est_visitante_2': prob_est_visitante_2,
                'prob_est_visitante_M': prob_est_visitante_M,
                'rentabilidad_local_0': rentabilidad_local_0,
                'rentabilidad_local_1': rentabilidad_local_1,
                'rentabilidad_local_2': rentabilidad_local_2,
                'rentabilidad_local_M': rentabilidad_local_M,
                'rentabilidad_visitante_0': rentabilidad_visitante_0,
                'rentabilidad_visitante_1': rentabilidad_visitante_1,
                'rentabilidad_visitante_2': rentabilidad_visitante_2,
                'rentabilidad_visitante_M': rentabilidad_visitante_M
            }
        )
        print('Se han cargado/actualizado los partidos de la jornada', jornada_actual,
              'en las bases Partido y PartidoPleno15')


if __name__ == "__main__":
    print('Por favor espere...')
    carga_partidos()
