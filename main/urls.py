from django.urls import path
from . import views

urlpatterns = [
    path('level-selection/', views.level_selection_view, name='level_selection'),
    path('level-selection/success/', views.level_selection_success, name='level_selection_success'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
