from django.urls import path,include
from .views import Homepage, Homefilmes, Detalhefilme, teste

app_name="filme"
urlpatterns = [
    path('teste/', teste, name='teste'),
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhefilme.as_view(), name="detalhesfilme")
]