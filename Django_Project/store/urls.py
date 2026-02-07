from django.urls import path
from store.views import (
    index, about, products, products_json, product_detail,
    add_product, update_product, delete_product
)

from store.views import (
    ProductListView, ProductDetailView, AddProductView,
    UpdateProductView, DeleteProductView, IndexView
)

from django.views.generic import TemplateView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products.json/', products_json, name='products_json'),
    path('product/<int:product_pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', UpdateProductView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', DeleteProductView.as_view(), name='delete_product'),
]