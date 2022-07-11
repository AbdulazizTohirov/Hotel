from django.db import models

class RoomsModel(models.Model):
    img = models.ImageField()

    def __str__(self):
        return self.img

class WorkersModel(models.Model):
    status = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.status

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
