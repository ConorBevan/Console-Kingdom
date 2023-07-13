from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('edit/<item_id>/', views.edit_cart_quantity, name='edit_cart_quantity'),
    path('delete/<item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
