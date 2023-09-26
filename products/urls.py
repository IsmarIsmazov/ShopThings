from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name='products'),
    path('create/', views.createproduct, name='create'),
    path("<int:pk>", views.ProductDetail.as_view(), name='product_detail')
]