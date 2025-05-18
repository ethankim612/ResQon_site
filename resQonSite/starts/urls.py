from django.urls import path
from . import views

app_name = 'starts'

urlpatterns = [
    path('', views.starts_view, name='starts'),
] 