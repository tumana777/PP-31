from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api.serializers import (
    CategoryListSerializer, ProductListSerializer, ProductDetailSerializer,
    TagListSerializer, ProductCreateSerializer, ProductUpdateSerializer
)
from store.models import Product, Category, Tag
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


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

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated]

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    permission_classes = [IsAuthenticated]

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductListSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductUpdateSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'title'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        return ProductUpdateSerializer

    # @action(detail=True, methods=['post'])
    # def change_availability_to_false(self, request, title=None):
    #     product = self.get_object()
    #     product.is_available = False
    #     product.save()
    #     return Response({
    #         'message': 'Product availability changed successfully.'
    #         , 'status': status.HTTP_200_OK
    #     })
    #
    # @action(detail=True, methods=['post'])
    # def change_availability_to_true(self, request, title=None):
    #     product = self.get_object()
    #     product.is_available = True
    #     product.save()
    #     return Response({
    #         'message': 'Product availability changed successfully.',
    #         'status': status.HTTP_200_OK
    #     })

    @action(detail=True, methods=['post'])
    def toggle_availability(self, request, title=None):
        product = self.get_object()
        product.is_available = not product.is_available
        product.save()
        return Response({
                'message': 'Product availability changed successfully.',
                'status': status.HTTP_200_OK
            })














