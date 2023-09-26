from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name='products'),
    path('create/', views.createproduct, name='create'),
]