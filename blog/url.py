from django.urls import path
from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.TagsView.as_view(), name='tag'), # выкладывание постов по тегам
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post"), # детальный вывод статьи
    path('<slug:category_name>/', views.CategoryView.as_view(), name="category"), # вывод статей по категориям
    path('', views.HomeVew.as_view(), name="home")# домашняя страница и вывод всех статей
]

