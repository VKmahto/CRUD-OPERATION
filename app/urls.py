from django.urls import path
from .import views

urlpatterns = [
    path('',views.base, name='base'),
    path('base/',views.base, name='base'),
    path('add/',views.brand,name='add'),
    path('brand_add/', views.brand, name='brand_add'),
    path('add/base.html', views.base, name='base'),
    path('base/brand_add/', views.brand, name='brand_add'),
    #for supplier
    path('basesupplier/',views.basesupplier,name='basesupplier'), 
    path('supplier/',views.add_supplier, name='supplier'),
    # path('submitform/',views.submitform),
]