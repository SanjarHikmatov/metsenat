from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.utils.models.base_model import BaseModel


class StudentSponsor(BaseModel):

    sponsor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="studensponsor_sponsors",
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'sponsor'},

    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="studentsponsor_students",
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'student'},
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )

    # def clean(self):
    #     if self.amount > self.sponsor.available:
    #         raise ValidationError({'amount': "Amount must be greater than sponsor's available."})
    #
    #     if self.amount > self.student.available:
    #         raise ValidationError({'amount': "Amount must not exceed the student's available balance."})
    #     #
    #     # if self.student.contract_amount == 0 or self.student.contract_amount < 0:
    #     #     raise ({'contract_amount': "Student's contract amount must be greater than 0."})
    #     #
    #     # if self.student.contract_amount >= self.student.balance:
    #     #     raise ({"contract_amount": 'Student already has enough balance to cover the contract amount.'})

    # def save(self, *args, **kwargs):
    #     if self.student.contract_amount == 0 or self.student.contract_amount < 0:
    #         self.student.balance += self.amount
    #     if self.sponsor.amount > 0:
    #         self.sponsor.balance -= self.amount
    #     self.clean()
    #     super().save(*args, **kwargs)