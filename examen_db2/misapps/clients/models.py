from django.db import models
from misapps.reservations.models import Reservations

class Clients(models.Model):
    name =models.CharField(max_length=100,help_text="Nommbre del cliente", verbose_name="Nombre del cliente")
    email=models.EmailField(max_length=100,help_text="Email del cliente",verbose_name="Email del cliente")
    fk_Resevations = models.ManyToManyField(Reservations, through='ClientsReservs', verbose_name="reservas cliente")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class ClientsReservs(models.Model):
    ClientsId= models.ForeignKey(Clients,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE,)
                                
    ReservationsId = models.ForeignKey(Reservations,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE,verbose_name="Reservas")

    SitioTuristico = models.CharField(max_length=100,help_text="Nombre del sitio turistico",verbose_name="Nombre del sitio turistico")

    def __str__(self):
        return self.SitioTuristico

    class Meta:
        verbose_name = "Reserva Cliente"
        verbose_name_plural = "Reservas Clientes"
    
      