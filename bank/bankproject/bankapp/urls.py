from django.urls import path

from bankapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('Welcome/', views.Welcome, name='Welcome')

]