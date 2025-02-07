from django.contrib.auth.models import Group, Permission

from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.db.models import Q

from apps.users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def post_save_user(instance: CustomUser, created: bool, **kwargs):
    if created:
        instance.add_to_group()
