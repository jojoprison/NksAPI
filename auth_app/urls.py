from django.urls import path

from .views import *


urlpatterns = [
    path('user/', PersonalRoomViewSet.as_view({'get': 'retrieve'})),
]
