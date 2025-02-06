from django.core.validators import RegexValidator

uzb_phone_number_validators = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Enter a valid phone number',
    code='invalid'
)