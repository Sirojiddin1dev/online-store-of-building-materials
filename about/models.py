from django.db import models


class About(models.Model):
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='about_photo/')

    def __str__(self):
        return self.text


class About1(models.Model):
    text = models.CharField(max_length=200)
    text1 = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Brand(models.Model):
    logo = models.ImageField(upload_to='logo_brand/')
