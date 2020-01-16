from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post"), # запускаем гет метод класса
    path('<slug:category_name>/', views.CategoryView.as_view(), name="category"), # запускаем гет метод класса
    path('', views.HomeVew.as_view())# запускаем гет метод класса
]

