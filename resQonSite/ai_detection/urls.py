from django.urls import path
from . import views

app_name = 'ai_detection'

urlpatterns = [
    path('', views.ai_detection_view, name='ai_detection'),
] 