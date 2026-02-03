from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('date/', views.curr_date),
    path('Car/<str:car>/', views.cars), # argument name and route name should be same
    path('book/', views.book),
    path('login/', views.login),
    path('about/', views.about),
    path('menu/', views.menu),
    path('book/', views.book),
]