from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='news_photo/')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    tag = models.ManyToManyField('Tag')
    view = models.IntegerField(default=0)
    video = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.CharField(max_length=55)

    def __str__(self):
        return self.email


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
