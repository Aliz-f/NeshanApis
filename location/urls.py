from django.urls import path
from .views import NeshanLocation
urlpatterns = [
    path('location/', NeshanLocation.as_view())
]
