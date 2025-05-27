from django.core.management.base import BaseCommand
from faker import Faker
from misapps.reservations.models import Reservations
from misapps.clients.models import Clients, ClientsReservs  # Ajusta según tu estructura real

class Command(BaseCommand):
    help = 'Popula la base de datos con datos falsos para Clients, Reservations y ClientsReservs'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Cantidad de registros a crear
        num_clients = 20
        num_reservations = 40
        num_clients_reservs = 50

        self.stdout.write('Borrando datos existentes...')
        ClientsReservs.objects.all().delete()
        Reservations.objects.all().delete()
        Clients.objects.all().delete()

        self.stdout.write('Creando clientes...')
        clients = []
        for _ in range(num_clients):
            client = Clients.objects.create(
                name=fake.name(),
                email=fake.email()
            )
            clients.append(client)
        self.stdout.write(f'{num_clients} clientes creados.')

        self.stdout.write('Creando reservaciones...')
        reservations = []
        for _ in range(num_reservations):
            reservation = Reservations.objects.create(
                DateReserv=fake.date_time_this_year(),
                NumDias=fake.random_int(min=1, max=15),
                valor=round(fake.random_number(digits=5, fix_len=False) / 100, 2)
            )
            reservations.append(reservation)
        self.stdout.write(f'{num_reservations} reservaciones creadas.')

        sitios_turisticos = [
            "Parque Nacional", "Museo de Arte", "Playa Azul", "Montaña Verde",
            "Reserva Natural", "Centro Histórico", "Acuario", "Zona Arqueológica"
        ]

        self.stdout.write('Creando clientes-reservaciones...')
        for _ in range(num_clients_reservs):
            client = fake.random_element(elements=clients)
            reservation = fake.random_element(elements=reservations)
            sitio = fake.random_element(elements=sitios_turisticos)

            ClientsReservs.objects.create(
                ClientsId=client,
                ReservationsId=reservation,
                SitioTuristico=sitio
            )
        self.stdout.write(f'{num_clients_reservs} registros de ClientsReservs creados.')

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con éxito!'))
