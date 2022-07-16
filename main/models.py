from unicodedata import name
from django.db import models

class RoomsModel(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    price =models.CharField(max_length=255) 

    def __str__(self):
        return self.title

class Rooms1Model(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    price =models.CharField(max_length=255) 

    def __str__(self):
        return self.title

class Rooms2Model(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    price =models.CharField(max_length=255) 

    def __str__(self):
        return self.title

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



class BookModel(models.Model):
    first_date = models.DateField()
    last_date = models.DateField()  
    Room_1 = 'Room_1'
    Room_2 = 'Room_2'
    Room_3 = 'Room_3'
    Room_4 = 'Room_4'
    Room_5 = 'Room_5'
    Rooms_Choices = [
        (Room_1, 'Room_1'),
        (Room_2, 'Room_2'),
        (Room_3, 'Room_3'),
        (Room_4, 'Room_4'),
        (Room_5, 'Room_5'),
    ]
    rooms_choices = models.CharField(
        max_length=255,
        choices=Rooms_Choices,
        default=Room_1,
    )
    guest_1 = 'guest_1'
    guest_2 = 'guest_2'
    guest_3 = 'guest_3'
    guest_4 = 'guest_4'
    guest_5 = 'guest_5'
    Guest_Choices = [
        (guest_1, 'guest_1'),
        (guest_2, 'guest_2'),
        (guest_3, 'guest_3'),
        (guest_4, 'guest_4'),
        (guest_5, 'guest_5'),
    ]
    guest_choices = models.CharField(
        max_length=255,
        choices=Guest_Choices,
        default=guest_1,
    )
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.Room_1