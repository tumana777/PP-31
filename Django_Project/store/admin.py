from django.contrib import admin
from store.models import Category, Product, Tag

# admin.site.register([Category, Product, Tag])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'total_price', 'is_available')
    list_display_links = ('title',)
    # list_filter = ('is_available', 'price')
    # list_per_page = 3
    list_editable = ('is_available', 'price', 'quantity')
    search_fields = ('description', 'title')
    readonly_fields = ('created_at', 'updated_at')
    actions = ['make_available', 'make_not_available']

    @admin.action(description='Make Products Available')
    def make_available(self, request, queryset):
        queryset.update(is_available=True)

    @admin.action(description='Make Products Not Available')
    def make_not_available(self, request, queryset):
        queryset.update(is_available=False)

    @admin.display(description='Total Price')
    def total_price(self, obj):
        return obj.price * obj.quantity

admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Test'
