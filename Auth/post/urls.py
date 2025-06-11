from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_view, name='create'), 
    path('list/', views.list_view, name='list'), 
    path('read/<int:id>/', views.read_view, name='read'),
    path('update/<int:id>/', views.update_view, name='update'),
]