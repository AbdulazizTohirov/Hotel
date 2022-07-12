from unicodedata import name
from django.db import models

class RoomsModel(models.Model):
    img = models.ImageField()

    def __str__(self):
        return self.img

class WorkersModel(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    img = models.ImageField(upload_to='staff')

    def __str__(self):
        return self.name

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
