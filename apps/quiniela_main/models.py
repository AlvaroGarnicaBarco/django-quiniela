from django.db import models


class Jornada(models.Model):
    temporada = models.CharField(max_length=9)
    num_jornada = models.IntegerField()
    liga_1 = models.CharField(max_length=24, )
    liga_2 = models.CharField(max_length=24, blank=True)
    liga_3 = models.CharField(max_length=24, blank=True)
    dia_inicio = models.DateField()
    dia_fin = models.DateField()
    recaudacion_estimada = models.DecimalField(max_digits=10, decimal_places=2)
    bote = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'jornada {self.num_jornada} ({self.temporada})'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['temporada', 'num_jornada'], name='unique_jornada')
        ]


class Partido(models.Model):
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    orden_partido = models.IntegerField()
    dia = models.CharField(max_length=3)
    hora = models.CharField(max_length=5)
    local = models.CharField(max_length=30)
    visitante = models.CharField(max_length=30)
    prob_real_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_X = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_2 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_X = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_2 = models.DecimalField(max_digits=2, decimal_places=0)
    rentabilidad_1 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_X = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_2 = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'jornada {self.jornada.num_jornada} - {str(self.orden_partido)} . {self.local} - {self.visitante}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['jornada', 'orden_partido'], name='unique_partido')
        ]


class PartidoPleno15(models.Model):
    jornada = models.OneToOneField(Jornada, on_delete=models.CASCADE)
    dia = models.CharField(max_length=3)
    hora = models.CharField(max_length=5)
    local = models.CharField(max_length=30)
    visitante = models.CharField(max_length=30)
    prob_real_local_0 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_local_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_local_2 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_local_M = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_visitante_0 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_visitante_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_visitante_2 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_real_visitante_M = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_local_0 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_local_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_local_2 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_local_M = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_visitante_0 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_visitante_1 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_visitante_2 = models.DecimalField(max_digits=2, decimal_places=0)
    prob_est_visitante_M = models.DecimalField(max_digits=2, decimal_places=0)
    rentabilidad_local_0 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_local_1 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_local_2 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_local_M = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_visitante_0 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_visitante_1 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_visitante_2 = models.DecimalField(max_digits=4, decimal_places=2)
    rentabilidad_visitante_M = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'jornada {self.jornada.num_jornada} {self.local} - {self.visitante}'

    class Meta:
        verbose_name_plural = "Partidos pleno 15"


class Jugada(models.Model):
    PARTIDO_CHOICES = [
        ('1', '1'),
        ('X', 'X'),
        ('2', '2'),
    ]
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    combinacion = models.CharField(max_length=14, unique=True)
    pos_est = models.IntegerField()
    pos_real = models.IntegerField()
    unos = models.IntegerField()
    equis = models.IntegerField()
    doses = models.IntegerField()
    mas_probs = models.IntegerField()
    menos_probs = models.IntegerField()
    partido_1 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_2 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_3 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_4 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_5 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_6 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_7 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_8 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_9 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_10 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_11 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_12 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_13 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)
    partido_14 = models.CharField(max_length=1, choices=PARTIDO_CHOICES)

    def __str__(self):
        return f'{self.combinacion} ({self.pos_real}th pos. real)'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['jornada', 'combinacion'], name='unique_jugada')
        ]