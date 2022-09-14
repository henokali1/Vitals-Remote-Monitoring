# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('live/', views.live, name='live.html'),
]
