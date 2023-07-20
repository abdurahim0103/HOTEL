from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length = 255)
    adres = models.CharField(max_length=255)
    creat_at = models.DateField()
    def __str__(self):
        return self.name
class RoomType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Room(models.Model):
    person_count = models.IntegerField()
    price_per_night = models.FloatField()
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, null = True)
    roomtype = models.ForeignKey(RoomType, on_delete= models.CASCADE, null= True)
    def __str__(self):
        return self.hotel.name
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    password_number = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name
class Booking(models.Model):
    total_price = models.FloatField(max_length=255)
    is_online = models.BooleanField()
    enter_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete= models.CASCADE, null= True)

class BookedPerson(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, null= True)
    booking = models.ForeignKey(Booking, on_delete= models.CASCADE, null= True)

class RatingCategory(models.Model):
    name = models.CharField(max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, null=True)
    def __str__(self):
        return self.name
class Rating(models.Model):
    score = models.FloatField()
    text = models.TextField()
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, null=True)
    booking = models.ForeignKey(Booking, on_delete= models.CASCADE, null=True)
    rating_info = models.IntegerField()
    

