from decimal import Decimal

from django.db import models
from django.conf import settings
from django.core import exceptions
from django.core.validators import MinValueValidator

from apps.utils.models.base_model import BaseModel


class StudentSponsor(BaseModel):

    sponsor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sponsors",
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'sponsor'},

    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="students",
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'student'},
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0"))],
    )

    def clean(self):

        if not self.amount:
            raise exceptions.ValidationError({'amount': "This field required"})

        if self.amount and self.amount > self.sponsor.available:
            raise exceptions.ValidationError(
                {f'available_balance': f"amount more then sponsor available balance ({self.amount} > {self.sponsor.available})"})

    def save(self, *args, **kwargs):
        self.clean()
        super(StudentSponsor, self).save(*args, **kwargs)



