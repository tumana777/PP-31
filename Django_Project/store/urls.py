from django.urls import path
from store.views import index, about, products, products_json, product_detail

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('products.json/', products_json, name='products_json'),
    path('product/<str:product_pk>/', product_detail, name='product_detail'),
]