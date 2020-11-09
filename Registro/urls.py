from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.menu),
    path('listaUsuarios',views.Usuario_list),

    path('', views.Usuario_list, name='usuario_list'),
    path('usuario/<int:pk>/', views.usuario_detail, name='usuario_detail'),

    path('usuario/new/',views.usuario_new, name='usuario_new'),
    #path('usuario/<int:pk>/new/',views.usuario_edit, name='usuario_edit'),


    path('top2020',views.top2020),
    path('top2019',views.top2019),
    path('noticias',views.noticias),    
]
