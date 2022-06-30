from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),

   
   
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/detail/<int:pk>/',views.staff_detail,name='dashboard-staff-detail'),
    path('staff/delete/<int:pk>/',views.staff_delete,name='dashboard-staff-delete'),

   
   
    path('order/',views.order,name='dashboard-order'),
    path('order/delete/<int:pk>/',views.order_delete,name='dashboard-order-delete'),
    path('order/update/<int:pk>/',views.order_update,name='dashboard-order-update'),


    
    
    
    path('product/',views.product,name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    
    
    
    path('provider/',views.provider,name='dashboard-provider'),
    path('provider/delete/<int:pk>/',views.provider_delete,name='dashboard-provider-delete'),
    path('provider/update/<int:pk>/',views.provider_update,name='dashboard-provider-update'),
    
    
]