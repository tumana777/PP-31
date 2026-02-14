from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    image = models.ImageField(upload_to='product_images', null=True, blank=True, default='default.jpg')
    tags = models.ManyToManyField(Tag, related_name='products')

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.category} --> {self.title}"




















