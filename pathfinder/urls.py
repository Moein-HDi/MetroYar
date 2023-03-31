from django.urls import path 
from .views import  HomePageView, StationsView, MapView


urlpatterns = [
    
    path('', HomePageView, name='home'),
    # path('map', MapView, name='map'),
    path('stations', StationsView, name='stations'),
]