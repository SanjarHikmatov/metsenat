from decimal import Decimal

from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

from apps.general.models import PaymeMethod
from apps.users.models import CustomUser
from apps.utils.models.base_model import BaseModel
from apps.general.validation_call_number import uzb_phone_number_validators


class Appeal(BaseModel):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        MODERATED = 'moderated', 'Moderated'
        VERIFIED = 'verified', 'Verified'
        CANCELED = 'canceled', 'Canceled'

    sponsor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='appeals_sponsor',
        verbose_name='Sponsor',
        limit_choices_to={'role': CustomUser.Role.SPONSOR}
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        help_text='Enter the amount money'
    )
    is_verified = models.BooleanField(default=False, editable=False)
    pay_method = models.ForeignKey(
        PaymeMethod,
        on_delete=models.PROTECT,
        related_name='appeal_pay_method',
        help_text='Choose the pay method'
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[uzb_phone_number_validators],
        help_text='Enter lake this Call number +998 99 999 99 99',

    )
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.NEW,
    )
    balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        editable=False,
    )

    def save(self, *args, **kwargs):

        if self.status == Appeal.Status.VERIFIED:
            self.sponsor.balance += self.amount
            self.sponsor.available += self.amount
            self.sponsor.save()

        if not self.pk:
            self.available = self.amount
        return super(Appeal, self).save(*args, **kwargs)



    class Meta:
        verbose_name = 'Appeal'


    def __str__(self):
        return f'Appeal {self.phone_number} - {self.amount}'
