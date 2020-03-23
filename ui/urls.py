from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/update/', views.update, name='update'),
]