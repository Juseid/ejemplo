from django.contrib import admin
from misapps.reservations.models import Reservations

# Register your models here.

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('NumDias', 'valor')
    # pass

admin.site.register(Reservations, ReservationsAdmin)