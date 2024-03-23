from django.db import models


class About(models.Model):
    text = models.TextFile()
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='about_photo/')

    def __str__(self):
        return self.text



