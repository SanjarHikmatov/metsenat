from django.db import models

class Appeal(models.Model):
    sponsor = models.ForeignKey(
        'sponsors.StudentSponsor',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    available = models.BooleanField()
    amount = models.PositiveSmallIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    pay_method = models.ForeignKey('general.PaymeMethod', on_delete=models.CASCADE)
