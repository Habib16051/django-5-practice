from django.urls import path
from . import views



urlpatterns = [
    path('', views.introduction, name='intro'),
    path('home/', views.home_view, name='home'),

]