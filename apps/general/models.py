from django.db import models

class PaymeMethod(models.Model):
    name = models.CharField(max_length=100)


class University(models.Model):
    name = models.CharField(max_length=100)
    contract_amount = models.PositiveSmallIntegerField(default=0)