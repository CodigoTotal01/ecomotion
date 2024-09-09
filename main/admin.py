from django.contrib import admin
from .models import Category , Brand , Color, Size, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'color', 'size', 'price', 'brand')

admin.site.register(Product, ProductAdmin)



