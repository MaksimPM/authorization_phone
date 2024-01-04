from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=12, unique=True, verbose_name='номер телефона')
    otp_code = models.CharField(max_length=4, verbose_name='код подтверждения')

    invite_code = models.CharField(max_length=6, blank=True, verbose_name='инвайт код')
    other_profile_invite_code = models.CharField(max_length=6, blank=True)

    inviter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='invited_users')

    def __str__(self):
        return self.phone_number

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)

    def check_otp_code(self, otp_code):
        """
        Метод проверяет соответствие кода подтверждения пользовательскому коду подтверждения.
        """
        return self.otp_code == otp_code

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
