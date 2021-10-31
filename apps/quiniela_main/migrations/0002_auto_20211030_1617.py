# Generated by Django 3.2.7 on 2021-10-30 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidopleno15',
            name='jornada',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiniela_main.jornada'),
        ),
        migrations.AddConstraint(
            model_name='jornada',
            constraint=models.UniqueConstraint(fields=('temporada', 'num_jornada'), name='unique_jornada'),
        ),
        migrations.AddConstraint(
            model_name='jugada',
            constraint=models.UniqueConstraint(fields=('jornada', 'combinacion'), name='unique_jugada'),
        ),
        migrations.AddConstraint(
            model_name='partido',
            constraint=models.UniqueConstraint(fields=('jornada', 'orden_partido'), name='unique_partido'),
        ),
    ]