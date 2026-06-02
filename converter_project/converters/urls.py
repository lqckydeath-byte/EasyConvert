from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('square/', views.square, name='square'),
    path('cube/', views.cube, name='cube'),
    path('temperature/', views.temperature, name='temperature'),
    path('luck/', views.luck, name='luck'),
    path('weight/', views.weight, name='weight'),
    path('memory/', views.memory, name='memory'),
    path('time/', views.vremya, name='time'),
]
