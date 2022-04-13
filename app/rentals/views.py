from rentals.selectors import read_reservations_table
from django.views.generic import ListView

# Create your views here.


class ReservationListView(ListView):
    paginate_by = 15
    queryset = read_reservations_table()
