from django.db import models
from django.utils.timezone import now


# Create your models here.
class Reservations(models.Model):
    # name = models.CharField(max_length=100, help_text="Nombre del documento", verbose_name="Nombre del documento")
    DateReserv = models.DateTimeField(default=now, verbose_name="Fecha de reservacion")
    NumDias = models.IntegerField(default=1, verbose_name="Numero de dias", help_text="Numero de dias")
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor", help_text="Valor")
    
    # def __int__(self):
    #     return str("reservacion numero ",self.valor)
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

