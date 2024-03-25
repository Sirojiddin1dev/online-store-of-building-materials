from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone


class User(AbstractUser):
    bio = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ),
    ])
    login_count = models.PositiveIntegerField(default=0)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def update_login_info(self):
        self.login_count += 1
        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return self.username
