from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year_id>/model', views.model, name='model'),
    path('cars', views.cars, name='cars'),
    path('<int:id>', views.detail, name='detail'),
    path('add_car', views.add_car, name='add_car'),
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('home', views.home, name='home'),
    path('car_parts', views.car_parts, name='car_parts'),
    path('add_car_parts', views.add_car_parts, name='add_car_parts'),
    path('accessories', views.accessories, name='accessories'),
    path('add_accessories', views.add_accessories, name='add_accessories'),
    path('problem', views.problem, name='problem'),
    path('add_problem', views.add_problem, name='add_problem'),
    path('craftsman', views.craftsman, name='craftsman'),
    path('youtube', views.youtube, name='youtube'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
