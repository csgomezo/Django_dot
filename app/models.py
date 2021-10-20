from django.db import models

# Create your models here.
class socio(models.Model):
    nombre = models.CharField(
        max_length=30
    )
    tasa = models.FloatField() #La tasa se guarda en valor sin porcentaje, después hay que procesarlo
    montoDisponible =  models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre= self.nombre.upper()
        super(socio,self).save()

    class Meta:
        verbose_name_plural = "socios"

class prestamo(models.Model):
    socio = models.CharField(
        max_length=30
    )
    cuota_mensual = models.FloatField()
    pagoTotal = models.IntegerField()
    tasaInteresM = models.FloatField()

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre= self.nombre.upper()
        super(prestamo,self).save()

    class Meta:
        verbose_name_plural = "prestamos"