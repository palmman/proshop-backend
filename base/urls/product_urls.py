from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.ProductsAPIView.as_view() , name='products'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view() , name='product'),
]
