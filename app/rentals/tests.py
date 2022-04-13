from operator import attrgetter, itemgetter
from pprint import pprint
from django.test import TestCase
from datetime import date

from rentals.models import Rental, Reservation
from rentals.selectors import read_reservations_table

# Create your tests here.


class TestSelectors(TestCase):
    def setUp(self):
        self.r1, self.r2 = Rental.objects.bulk_create([
            Rental(name='Rental-1'),
            Rental(name='Rental-2')
        ])
        self.reservations1 = Reservation.objects.bulk_create([
            Reservation(rental=self.r1, checkin=date(2022, 1, 1),
                        checkout=date(2022, 1, 13)),
            Reservation(rental=self.r1, checkin=date(2022, 1, 20),
                        checkout=date(2022, 2, 10)),
            Reservation(rental=self.r1, checkin=date(2022, 2, 20),
                        checkout=date(2022, 3, 10)),
        ])
        self.reservations2 = Reservation.objects.bulk_create([
            Reservation(rental=self.r2, checkin=date(2022, 1, 2),
                        checkout=date(2022, 1, 20)),
            Reservation(rental=self.r2, checkin=date(2022, 1, 20),
                        checkout=date(2022, 2, 11)),
        ])

    def test_read_reservations_table(self):
        reservations = read_reservations_table()
        assert reservations.count() == 5
        reservations = list(reservations)
        reservations1 = reservations[:-2]
        reservations2 = reservations[-2:]
        assert self.reservations1 == reservations1
        assert self.reservations2 == reservations2

        id_getter = attrgetter('id')
        prev_getter = attrgetter('previous_reservation')

        expected = [None, *map(id_getter, self.reservations1[:-1])]
        got = [*map(prev_getter, reservations1)]

        assert expected == got

        expected = [None, *map(id_getter, self.reservations2[:-1])]
        got = [*map(prev_getter, reservations2)]
        assert expected == got
