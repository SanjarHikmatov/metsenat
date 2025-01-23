from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.hashers import make_password

from apps.general.service import user_photo_location
from apps.general.validation_call_number import uzb_phone_number_validators
from django.core.exceptions import ValidationError
class CustomUserManager(UserManager):

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given username, phone_number, and password.
        """
        try:
            uzb_phone_number_validators(phone_number)
        except ValidationError:
            raise ValidationError("Invalid phone number format.")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, phone_number=None, password=None, **extra_fields):
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        extra_fields["is_staff"] = extra_fields["is_superuser"] = True
        return self._create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    class CustomType(models.TextChoices):
        personal = '0', 'Personal'
        legal = '1' 'Legal'


    username = None
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(
        upload_to=user_photo_location,
        null=True,
        blank=True
    )
    objects = CustomUserManager()
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # ======== Extra fields ===================
    user_type = models.CharField(max_length=10, choices=CustomType.choices, default=CustomType.personal)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    university = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    degree = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)

