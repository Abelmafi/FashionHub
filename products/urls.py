from django.urls import path
from app.views.product_view import *
from app.views.category_view import *
from app.views.cart_view import *
from .views import *
app_name = 'products'

urlpatterns = [
    path('category-list/', category_list, name='category_list'),
    path('product-list/', product_list, name='product_list'),
    path('product-detail/<int:id>/', product_detail, name='product_detail'),
    path('category/<slug>/', category_products, name='category_products'),
    path('product-detail/<int:pk>/add_to_cart/', add_to_cart, name='add_to_cart'),
  #  path('', views.ProductListView.as_view(), name='product_list'),
    path('add/', product_upload, name='product_upload'),
  #  path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
  #  path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
  #  path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]

