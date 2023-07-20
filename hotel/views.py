from django.shortcuts import render
from .models import Hotel, RoomType, Room, Customer, Booking, BookedPerson, RatingCategory, Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from .seriliazer import HotelSeriliazer, RoomTypeSeriliazer, RoomSeriliazer, CustomerSeriliazer
# Create your views here.
class GetHotel(APIView):
    def get(self,request):
        hotel=Hotel.objects.all()
        seriliazer=HotelSeriliazer(hotel,many=True)
        return Response(seriliazer.data)

class GetRoomType(APIView):
    def get(self,request):
        roomtype=RoomType.objects.all()
        seriliazer=RoomTypeSeriliazer(roomtype,many=True)
        return Response(seriliazer.data)

class GetRoom(APIView):
    def get(self,request):
        room=Room.objects.all()
        seriliazer=RoomSeriliazer(room,many=True)
        return Response(seriliazer.data)

class GetCustomer(APIView):
    def get(self,request):
        customer=Customer.objects.all()
        seriliazer=CustomerSeriliazer(customer,many=True)
        return Response(seriliazer.data)