from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('ajax/update/', views.update, name='update'),
]