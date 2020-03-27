from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.stat_view, name='info'),
    path('risk_scan', views.risk_scan, name='risk-scan'),
    path('ajax/update/', views.update, name='update'),
    path("bot/stat/", views.bot_stat_result, name='bot_stat')
]