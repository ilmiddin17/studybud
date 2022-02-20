from django.urls import path
from .views import home,create_room, room_detail

app_name='main'
urlpatterns=[
    path('', home, name='home'),
    path('create-room/', create_room, name='create_room'),
    path('room/<str:room_id>/', room_detail, name='room_detail'),
]