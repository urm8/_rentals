from django.db.models import F, Window
from django.db.models.functions import Lag
from rentals.models import Reservation


def read_reservations_table():
    return Reservation.objects.select_related('rental').order_by('rental', F(
        'checkout').asc(nulls_last=True)).annotate(
            previous_reservation=Window(
                expression=Lag('pk'),
                partition_by=[F('rental_id'), ],
                order_by=[F('rental_id'), F('checkout').asc(nulls_last=True)]),
    )
