from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('date/', views.curr_date),
    path('<str:car>/', views.cars), # argument name and route name should be same

]