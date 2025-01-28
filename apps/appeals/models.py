from decimal import Decimal

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError

from apps.utils.models.base_model import BaseModel
from apps.general.validation_call_number import uzb_phone_number_validators


class Appeal(BaseModel):


    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        help_text='Enter the amount money'
    )
    is_verified = models.BooleanField(default=False)
    pay_method = models.ForeignKey(
        'general.PaymeMethod',
        on_delete=models.PROTECT,
        related_name='pay_method', help_text='Choose the pay method'
    )


    phone_number = models.CharField(
        max_length=13,
        validators=[uzb_phone_number_validators],
        help_text='Enter lake this Call number +998 99 999 99 99'

    )
    full_name = models.CharField(max_length=255, help_text='Please enter Full Name')
    organization = models.CharField(max_length=255, help_text='Enter your Organization')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.phone_number)
        if Appeal.objects.filter(slug=self.slug).exists():
            raise ValidationError({'phone_number': "Your call number already exists, please enter the other call number"})
        super(Appeal, self).save(*args, **kwargs)

    def __str__(self):
        return f'Appeal {self.phone_number} - {self.amount}'