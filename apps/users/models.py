from django.db import models
from decimal import Decimal
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, RegexValidator

from apps.general.models import University
from apps.utils.models.base_model import BaseModel
from apps.general.service import user_photo_location
from django.core.exceptions import ValidationError
from apps.general.validation_call_number import uzb_phone_number_validators


class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number, and  send some code for login.
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


class CustomUser(BaseModel, PermissionsMixin):

    class Role(models.TextChoices):
        sponsor = 'sponsor', 'Sponsor'
        student = 'student', 'Student'
        admin = 'admin', 'Admin'


    class StudentDegree(models.TextChoices):
        BACHELOR = 'bachelor', 'Bachelor'
        MASTER = 'master', 'Master'
        EMPTY = 'empty', 'Empty'


    class LegalType(models.TextChoices):
        JURIDIC = 'juridic', 'Juridic'
        PHYSICAL = 'physical', 'Physical'

    user_type = models.CharField(
        max_length=25,
        choices=LegalType.choices,
        default=LegalType.JURIDIC,
    )


    first_name = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message="Enter a valid first name.",
            )
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message="Enter a valid last name.",
            )
        ]
    )
    photo = models.ImageField(
        upload_to=user_photo_location,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[uzb_phone_number_validators])

    # ======== Extra fields ===================
    university = models.ForeignKey(
        University,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='student_university'
    )

    balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal(0),
        validators=[MinValueValidator(Decimal(0))]

    )
    available = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal(0),
        validators=[MinValueValidator(Decimal(0))],
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,

    )

    student_degree = models.CharField(
        max_length=50,
        choices=StudentDegree.choices,
        default=StudentDegree.EMPTY,
    )

    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        if (
                not self.Role.student
                or not
                self.university
                or not
                self.student_degree

        ):
            raise ValidationError({'student': "You not entered your Role should student and you enter university and student degree."})

    def __str__(self):
        return f'User name {self.first_name},  user type {self.get_role_display()}'

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True


