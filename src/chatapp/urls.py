from django.urls import path
from . import views


urlpatterns= [
    path('',views.CreateRoom,name="create-room"),
    path('<str:room>/<str:username>/',views.MessageView,name="room"),
]