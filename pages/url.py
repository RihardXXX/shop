from django.urls import path
from . import views

urlpatterns = [
    path('<slug:url>', views.AboutView.as_view(), name="page"),
]