from rest_framework import serializers
from store.models import Product, Category


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    product_count = serializers.IntegerField()

# class CategoryListSerializer(serializers.ModelSerializer):
#
#     dasaxeleba = serializers.CharField(source='title')
#
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         exclude = ['title']