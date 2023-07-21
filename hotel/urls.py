from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("hotels/",views.GetHotel.as_view() ),
    path("room_type/",views.GetRoomType.as_view() ),
    path("room/",views.GetRoom.as_view() ),
    path("customer/",views.GetCustomer.as_view() ),
]
