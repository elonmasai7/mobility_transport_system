# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate_fare/', views.calculate_fare, name='calculate_fare'),
    # Add more paths for other views as needed
]
