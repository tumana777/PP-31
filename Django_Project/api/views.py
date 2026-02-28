from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import (
    CategoryListSerializer, ProductListSerializer, ProductDetailSerializer,
    TagListSerializer, ProductCreateSerializer
)
from store.models import Product, Category, Tag
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView


# @api_view(['GET'])
# def products_json(request):
#     products = Product.objects.values()
#     return Response({'products': products})

@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def products_list(request):
#     products = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
#     serializer = ProductListSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)

class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    serializer_class = ProductListSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_pk'

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]