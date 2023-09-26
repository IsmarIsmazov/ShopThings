from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name='products'),
    path('create/', views.createproduct, name='create'),
    path("<int:pk>", views.ProductDetail.as_view(), name='product_detail'),
    path("<int:pk>/update", views.ProductUpdate.as_view(), name='product_update'),
    path("<int:pk>/delete", views.ProductDelete.as_view(), name='product_delete')
]