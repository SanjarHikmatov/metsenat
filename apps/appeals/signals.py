from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.appeals.models import Appeal

#
# @receiver(post_save, sender=Appeal)
# def update_sponsor_status(sender, instance, **kwargs):
#     sponsor_appeals = Appeal.objects.filter(
#         sponsor=instance.sponsor,
#         status = Appeal.Status.VERIFIED
#     )
#     if sponsor_appeals.exists():
#         from django.db.models import F
#         sponsor_appeals.balance = F('balance') + instance.amount
#         instance.sponsor.save(update_fields=['balance'])
#
#



