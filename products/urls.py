from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('created/',views.product_created,name='product_create'),
    path('<int:id>/',views.product_detail,name='product_detail'),
    path('<int:id>/update/',views.product_update,name='product_updated'),
    path('<int:id>/delete/',views.product_delete,name='product_delete')
    
]