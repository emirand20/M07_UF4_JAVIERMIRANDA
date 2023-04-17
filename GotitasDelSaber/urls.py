from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.proff, name='proff'),
    path('', views.students, name='students'),
    path('proffs/proff/<int:tc>/', views.proff, name='proff'),
    path('proffs/', views.proffs, name='proffs'),
    path('students/student/<str:st>/', views.student, name='student'),
    path('students/', views.students, name='students'),
]