import json
import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
import redis

from apps.users.infrastructure.orm_models.models import *
from config import settings

PYMES_CUBA = [
    "Panadería Glez",
    "AlaSoluciones",
    "IVROTEC",
    "Pescadería Cafetería",
    "DFORJA",
    "ALTEC PRODUCCIONES",
    "Dofleini",
    "Cinesoft Recreación",
 ]
CIUDADES_CUBA = ["Habana", "Artemisa", "Matanzas", "Mayabeque"]
CDS_CUBA = ["CD Habana", "CD Santiago", "CD Matanzas"]
DRIVERS_FIRST_NAMES = [
    "Jose", "Ana", "Luis", "Alfred", "Sonia", "Regla", "Carlos", "Maria", "Pedro", "Isabel",
    "Miguel", "Yosvany", "Lucia", "Ernesto", "Raul", "Carmen", "Victor", "Gloria", "Rafael", "Diana"
]

DRIVERS_LAST_NAMES = [
    "Perez", "Rodriguez", "Gonzalez", "Martinez", "Hernandez", "Lopez", "Sanchez", "Diaz", "Alvarez", "Jimenez",
    "Torres", "Castro", "Rivera", "Mendez", "Fernandez", "Rojas", "Gomez", "Cabrera", "Vazquez", "Suarez"
]

PRODUCTS_CUBA = [
    {"sku": "PROD-001", "name": "Producto A", "description": "Descripción A"},
    {"sku": "PROD-002", "name": "Producto B", "description": "Descripción B"},
    {"sku": "PROD-003", "name": "Producto C", "description": "Descripción C"},
]
def get_or_create_pyme():
    name = random.choice(PYMES_CUBA)
    city = random.choice(CIUDADES_CUBA)
    pyme, _ = Pyme.objects.get_or_create(name=name, defaults={"city": city})
    return pyme

def get_or_create_cd():
    city= random.choice(CIUDADES_CUBA)
    name = f"CD {city}"
    city = city
    cd, _ = DistributionCenter.objects.get_or_create(name=name, defaults={"city": city})
    return cd


def get_or_create_product(sku):
    prod_info = next((p for p in PRODUCTS_CUBA if p["sku"] == sku), None)
    if not prod_info:
        prod_info = random.choice(PRODUCTS_CUBA)
    product, _ = Product.objects.get_or_create(
        sku=sku,
        defaults={"name": prod_info["name"], "description": prod_info["description"]}
    )
    return product

def get_random_order_status():
    return random.choice([status.value for status in OrderStatus])

def get_random_incidence_status():
    return random.choice([status.value for status in IncidenceStatus])


@transaction.atomic
def process_event(event):
    pyme = get_or_create_pyme()
    cd = get_or_create_cd()

    first_name = random.choice(DRIVERS_FIRST_NAMES)
    last_name = random.choice(DRIVERS_LAST_NAMES)
    driver_defaults = {
        "name": f"{first_name} {last_name}",
        "phone": f"+53{random.randint(10000000, 99999999)}",
        "email": f"{first_name.lower()}.{last_name.lower()}@cuba.cu",
    }
    driver, _ = Driver.objects.get_or_create(id=event["id_chofer"], defaults=driver_defaults)

    # Bloque
    block, _ = Block.objects.get_or_create(id=event["id_bloque"], defaults={"driver": driver})

    # Orden
    order_exists = Order.objects.filter(id=event["id_orden"]).exists()
    order, created = Order.objects.get_or_create(
        id=event["id_orden"],
        defaults={
            "pyme": pyme,
            "distribution_center": cd,
            "dispatch_date": datetime.strptime(event["fecha_despacho"], "%Y-%m-%d %H:%M:%S"),
            "status": get_random_order_status(),
            "total_weight": 0,
            "total_volume": 0,
        }
    )

    BlockOrder.objects.get_or_create(block=block, order=order)

    if not order_exists:
        productos = json.loads(event["productos"])
        total_weight, total_volume = 0, 0
        for prod in productos:
            product = get_or_create_product(prod["sku"])
            OrderProduct.objects.get_or_create(order=order, product=product, defaults={"quantity": prod["qty"]})
            total_weight += prod["qty"] * 1
            total_volume += prod["qty"] * 0.001

        order.total_weight = total_weight
        order.total_volume = total_volume
        order.save()

        # Generar incidencia aleatoria solo si es orden nueva
        if random.random() < 0.2:
            type_inc = random.choice(list(IncidenceType))
            Incidence.objects.create(
                id=uuid.uuid4(),
                order=order,
                type=type_inc.value,
                description=f"Incidencia generada automáticamente: {type_inc.name}",
                date=datetime.now(),
                status=get_random_incidence_status(),
            )

class Command(BaseCommand):
    help = 'Sincroniza bloques desde Redis y llena todas las tablas'

    def handle(self, *args, **kwargs):
        r = redis.Redis(
            host=getattr(settings, "REDIS_HOST", "localhost"),
            port=getattr(settings, "REDIS_PORT", 6379),
            db=getattr(settings, "REDIS_DB", 0)
        )

        last_id = '0'  # Empezar desde el primer mensaje
        print("Iniciando sincronización de bloques...")

        # Leer con timeout de 5 segundos
        events = r.xread({'logistrack.blocks': last_id}, count=None, block=5000)

        if not events:
            print("No hay eventos nuevos, terminando sincronización.")
            return

        for stream_name, messages in events:
            for message_id, message_data in messages:
                event = {k.decode(): v.decode() for k, v in message_data.items()}
                try:
                    process_event(event)
                except Exception as e:
                    print(f"Error procesando evento {message_id}: {e}")

            last_id = messages[-1][0]

        print("Sincronización completada")
