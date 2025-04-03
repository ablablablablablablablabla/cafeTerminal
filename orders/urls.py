# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='create_order'),
    path('revenue/', views.revenue_report, name='revenue_report'),
    path('update/<int:order_id>/', views.update_status, name='update_status'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
]