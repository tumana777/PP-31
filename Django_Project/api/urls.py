from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    categories_list, ProductListAPIView,
    ProductRetrieveAPIView, ProductCreateAPIView,
    TagListAPIView, ProductUpdateAPIView, ProductDeleteAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    ProductViewSet
)

router = DefaultRouter()

router.register('products', viewset=ProductViewSet)

app_name = 'api'

urlpatterns = [
    path('categories/', categories_list, name='categories'),
    path('tags/', TagListAPIView.as_view(), name='tags'),
    # path('products/', ProductListAPIView.as_view(), name='products'),
    # path('products/<int:product_pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    # path('create_product/', ProductCreateAPIView.as_view(), name='create_product'),
    # path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),
    # path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete_product'),
    # path('products/', ProductListCreateAPIView.as_view(), name='products'),
    # path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product'),
    path('', include(router.urls)),
]