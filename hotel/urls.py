from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("all_hotels/",views.GetHotel.as_view() ),
    path("RoomType/",views.GetRoomType.as_view() ),
    path("Room/",views.GetRoom.as_view() ),
    path("Customer/",views.GetCustomer.as_view() ),
]
