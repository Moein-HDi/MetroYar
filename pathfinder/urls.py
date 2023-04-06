from django.urls import path 
from .views import  HomePageView, StationsView, MapView, ReportView, PageNotFoundView, ServerErrorView


urlpatterns = [
    
    path('', HomePageView, name='home'),
    path('map', MapView, name='map'),
    path('stations', StationsView, name='stations'),
    path('report', ReportView, name='report'),
    path('404', PageNotFoundView, name='404'),
    path('500', ServerErrorView, name='500'),
]