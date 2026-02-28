from django.urls import path
from api.views import (
    categories_list, ProductListAPIView,
    ProductRetrieveAPIView, ProductCreateAPIView,
    TagListAPIView
)

app_name = 'api'

urlpatterns = [
    path('categories/', categories_list, name='categories'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:product_pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('create_product/', ProductCreateAPIView.as_view(), name='create_product'),
    path('tags/', TagListAPIView.as_view(), name='tags'),
]