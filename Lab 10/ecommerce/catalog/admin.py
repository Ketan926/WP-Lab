from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')  # Fields to display in the admin list view
    search_fields = ('title',)  # Add a search box for the title field

admin.site.register(Product, ProductAdmin)