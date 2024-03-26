from django.db import models
from django.core.validators import RegexValidator
from account.models import User


class Info(models.Model):
    logo = models.ImageField(upload_to='info_img/')
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code="Telefon raqam xato"
        )
    ])
    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.youtube


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code="Telefon raqam xato"
        )
    ])
    message = models.TextField()

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_img')

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='blog_img/')
    description = models.TextField()
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    message = models.TextField()