from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.proff, name='proff'),
    path('', views.students, name='students'),
    path('proff/', views.proff, name='proff'),
    path('students/', views.students, name='students'),
]