
from django.contrib import admin
from misapps.clients.models import Clients, ClientsReservs

# Register your models here.


class MembershipInline(admin.TabularInline):
    model = ClientsReservs
    extra = 1

class ClientsAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('name','email')

# class ReservationsAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)



admin.site.register(Clients, ClientsAdmin)