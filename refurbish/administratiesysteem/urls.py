from django.urls import path
from . import views

urlpatterns = [
    path('', views.computers, name='computers'),
    path('registratie', views.registratie, name='registratie'),
    path('post_registratie', views.post_registratie, name='post_registratie'),
    path('reparatie', views.reparatie, name='reparatie'),
    path('reparatie/<int:id>', views.reparatie_detail, name='reparatie_detail'),
    path('reparatie/post_reparatie/<int:id>', views.post_reparatie, name='post_reparatie'),
]