from django.urls import path
from .views import setDistance

urlpatterns = [
    path('', setDistance.as_view()),
]

