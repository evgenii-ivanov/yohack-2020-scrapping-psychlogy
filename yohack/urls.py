from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='yohack-home'),
    path('about/', views.about, name='yohack-about'),
    path('search/', views.search, name='yohack-search')
]