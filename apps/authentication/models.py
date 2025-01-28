"""# from django.db import models
    # from django.utils import timezone
    # from datetime import timedelta
    #
    # from apps.general.validation_call_number import uzb_phone_number_validators
    #
    #
    # class OTP(models.Model):
    #
    #
    #     phone_number = models.CharField(
    #         max_length=13,
    #         unique=True,
    #         validators=[uzb_phone_number_validators]
    #     )
    #     code = models.CharField(max_length=6)
    #     created_at = models.DateTimeField(auto_now_add=True)
    #
    #     class Meta:
    #         verbose_name = 'OTP'
    #         verbose_name_plural = 'OTPs'
    #         unique_together = ('code', 'phone_number')
    #
    #     def is_expired(self):
    #         return timezone.now() > self.created_at + timedelta(minutes=1)
    #
    #
    #     def __str__(self):
    #         return f"OTP for {self.phone_number}"
"""