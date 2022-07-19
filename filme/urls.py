from django.urls import path,include
from .views import homepage, homefilmes


urlpatterns = [
    path('', homepage, name='homepage'),
    path('filmes/', homefilmes, name='homefilmes'),
]