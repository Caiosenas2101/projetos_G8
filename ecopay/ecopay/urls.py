
from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.login, name="login"),
    path('home_aluno/', views.home_aluno, name="home_aluno") ,
    path('home_adm/', views.home_adm, name="home_adm") ,
    path('processar_formulario/', views.processar_formulario, name="processar_formulario"),

 ]