from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars', views.cars, name='cars'),
    path('<int:id>', views.detail, name='detail'),
    path('add_car', views.add_car, name='add_car'),
]
