from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.menu),
    path('listaUsuarios',views.Usuario_list),
    path('top2020',views.top2020),
    path('top2019',views.top2019),
    path('noticias',views.noticias)
]
