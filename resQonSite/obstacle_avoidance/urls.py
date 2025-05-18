from django.urls import path
from . import views

app_name = 'obstacle_avoidance'

urlpatterns = [
    path('', views.obstacle_avoidance_view, name='obstacle_avoidance'),
] 