from django.contrib import admin
from .models import Category, Product, ProductImage

# Kategori admin paneli
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Ürün resimleri için inline admin paneli
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Kaç tane boş resim alanı gösterileceğini belirtir

# Ürün admin paneli
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    inlines = [ProductImageInline]  # Ürün resimlerini ürün sayfasında göster

# Modelleri admin paneline kaydet
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)