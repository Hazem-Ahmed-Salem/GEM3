from django.urls import path
from .views import *

urlpatterns = [
    path("arts/<str:lang>",all_art,name="all_art"),
    path("art/<int:id>/<str:lang>",one_art,name="one_art"),
    path("art/",add_art,name="add_art"),
    
]