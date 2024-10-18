from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('registro/', views.Registro, name='registro'),
    path('login/', views.login, name='login'),
]
