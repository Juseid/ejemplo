# Generated by Django 5.0.14 on 2025-05-27 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('reservations', '0003_alter_reservations_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientsreservs',
            options={'verbose_name': 'Reserva Cliente', 'verbose_name_plural': 'Reservas Clientes'},
        ),
        migrations.AddField(
            model_name='clients',
            name='fk',
            field=models.ManyToManyField(through='clients.ClientsReservs', to='reservations.reservations', verbose_name='ClientsReservs'),
        ),
        migrations.AlterField(
            model_name='clientsreservs',
            name='ReservationsId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.reservations', verbose_name='Reservas'),
        ),
    ]
