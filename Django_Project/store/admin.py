from django.contrib import admin
from store.models import Category, Product

admin.site.register([Category, Product])
admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Test'
