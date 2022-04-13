from django.contrib import admin
from rentals.models import Rental, Reservation

admin.site.register(Rental, list_display=(
    'id', 'name'), search_fields=('name',))
admin.site.register(Reservation, list_display=(
    'rental', 'id', 'checkin', 'checkout'), list_select_related=('rental',), autocomplete_fields=('rental',), list_filter=('rental',))
# Register your models here.
