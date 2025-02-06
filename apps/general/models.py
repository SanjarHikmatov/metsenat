from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from apps.utils.models.base_model import BaseModel





class PaymeMethod(BaseModel):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if PaymeMethod.objects.filter(slug=self.slug).exclude().exists():
            raise ValidationError({'slug': "this payment method already exists, please enter the right name"})
        super(PaymeMethod, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class University(BaseModel):

    name = models.CharField(max_length=100)
    contract_amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    slug = models.SlugField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if University.objects.filter(slug=self.slug).exclude().exists():
            raise ValidationError({'slug': "this university already exists, please enter the right name"})
        super(University, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

