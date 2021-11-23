from django.urls import path
from .views import NeshanLocation
urlpatterns = [
    path('', NeshanLocation.as_view())
]
