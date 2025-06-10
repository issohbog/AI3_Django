from django.urls import path
from . import views

# product 앱의 url 패턴 정의 
app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),          # '' : /product
    path('cart/', views.cart_list, name='cart_list'),            # '/cart' : /product/cart
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'), 
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    
]