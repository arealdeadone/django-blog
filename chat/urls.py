from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat-main'),
    path('<str:room_name>/', views.room, name='chat-room')
]
