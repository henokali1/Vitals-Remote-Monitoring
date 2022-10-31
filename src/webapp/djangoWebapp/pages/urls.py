# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('live/', views.live, name='live.html'),
    path('update_live/', views.update_live, name='live.html'),
    path('vid/', views.vid, name='vid.html'),
    path('tst/', views.tst, name='tst.html'),
    path('historical_data/', views.historical_data, name='historical_data.html'),
    path('save_ip/', views.save_ip, name='tst.html'),
    path('get_ip/', views.get_ip, name='ip.html'),
    path('ip/', views.ip, name='ip.html'),
]
