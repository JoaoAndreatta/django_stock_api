from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stock/', views.stock, name='stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock/', views.delete_stock, name='delete_stock')
]
