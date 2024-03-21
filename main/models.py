from django.db import models
from django.core.validators import RegexValidator


class Info(models.Model):
    logo = models.ImageField(upload_to='info_img/')
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField( max_length=17, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code = "Telefon raqa, xato"
        )
    ])
    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.facebook


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
