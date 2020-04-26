from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='yohack-home'),
    path('about/', views.about, name='yohack-about'),
    path('search/', views.search, name='yohack-search'),
    path('register/', views.register, name='yohack-register'),
    path('login/', auth_views.LoginView.as_view(template_name='yohack/login.html'), name='yohack-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='yohack/logout.html'), name='yohack-logout'),
    path('profile/', views.profile, name='yohack-profile')
]