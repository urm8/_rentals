from django.db import models
from django.utils.timezone import now


class Rental(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.pk}, name={self.name})'


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.SET_NULL, null=True)
    checkin = models.DateField(null=False, default=now)
    checkout = models.DateField(null=True, blank=True, default=None)

    class Meta:
        ordering = ('rental', models.F('checkin').desc(nulls_first=True))

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.pk}, checkin={self.checkin.isoformat()}, checkout={self.checkout.isoformat() if self.checkout else None})'
