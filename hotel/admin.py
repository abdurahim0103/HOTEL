from django.contrib import admin
from .models import Hotel, RoomType, Room, Customer, Booking, BookedPerson, RatingCategory, Rating
# Register your models here.
admin.site.register(Hotel),
admin.site.register(RoomType),
admin.site.register(Room),
admin.site.register(Customer),
admin.site.register(Booking),
admin.site.register(BookedPerson),
admin.site.register(RatingCategory),
admin.site.register(Rating),
