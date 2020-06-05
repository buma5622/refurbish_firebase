from django.urls import path
from . import views

urlpatterns = [
    path('', views.computers, name='computers'),
    path('registratie', views.registratie, name='registratie'),
    path('post_registratie', views.post_registratie, name='post_registratie'),
]