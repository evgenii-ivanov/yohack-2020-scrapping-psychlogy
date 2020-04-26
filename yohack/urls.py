from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='yohack-home'),
    path('about/', views.about, name='yohack-about'),
    path('search/', views.PartnerListView.as_view(), name='yohack-search')
]