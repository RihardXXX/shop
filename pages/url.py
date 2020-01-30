from django.urls import path
from . import views

urlpatterns = [
    path('<path:url>', views.AboutView.as_view(), name="page"),
]