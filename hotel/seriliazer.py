from rest_framework import serializers
from .models import Hotel, RoomType, Room, Customer, Booking, BookedPerson, RatingCategory, Rating
class HotelSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields="__all__"

class RoomTypeSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=RoomType
        fields="__all__"

class RoomSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields="__all__"

class CustomerSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"