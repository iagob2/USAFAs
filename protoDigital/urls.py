from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('registro/', views.Registro, name='registro'),
    path('login/', views.login, name='login'),
    path('configuracoes/', views.Configuracoes, name='configuracoes'),
    path('cartao_virtual/', views.Cartao_Virtual, name='cartao_virtual'),
    path('marcar_consulta/', views.Marcar_Consulta, name='marcar_consulta'),
    path('perfil_do_usuario/', views.Perfil_do_Usuario, name='perfil_do_usuario'),
]
