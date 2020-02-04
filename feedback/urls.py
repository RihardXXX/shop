from django.urls import path
from .views import get_feedback

urlpatterns = [
    path('', get_feedback, name='feedback'), # выкладывание постов по тегам
]