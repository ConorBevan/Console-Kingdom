from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('subscribe', views.subscribe, name='subscribe'),
]
