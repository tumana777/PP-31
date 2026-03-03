from rest_framework import serializers
from store.models import Product, Category, Tag


# class CategoryListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     product_count = serializers.IntegerField()

class CategoryListSerializer(serializers.ModelSerializer):

    dasaxeleba = serializers.CharField(source='title')

    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ['title']

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']

class ProductDetailSerializer(serializers.ModelSerializer):

    category = serializers.ReadOnlyField(source='category.title')
    tags = TagListSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.price * obj.quantity

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['is_available']

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




















