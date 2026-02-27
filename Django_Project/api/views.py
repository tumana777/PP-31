from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CategoryListSerializer
from store.models import Product, Category


# @api_view(['GET'])
# def products_json(request):
#     products = Product.objects.values()
#     return Response({'products': products})

@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)