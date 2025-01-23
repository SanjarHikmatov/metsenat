from django.db import models
from django.conf import settings


class StudentSponsor(models.Model):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sponsors", on_delete=models.PROTECT)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="students", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
