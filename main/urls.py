from django.urls import path, re_path
from main import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.lol, name='home'),
    path('fak',views.fak,name='about'),
]