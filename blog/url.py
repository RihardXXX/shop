from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_name>/', views.CategoryView.as_view(), name="category"), # запускаем гет метод класса
    path('', views.HomeVew.as_view())# запускаем гет метод класса
]