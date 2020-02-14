from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name='home'),
    # path(r'^page/(\d+)/$', views.PostListView.as_view(), name='home'),
]