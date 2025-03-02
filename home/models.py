from django.db import models

# Kategori modeli
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori İsmi")
    description = models.TextField(blank=True, null=True, verbose_name="Kategori Açıklaması")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


# Ürün modeli
class Product(models.Model):
    # Ürün ID'si
    id = models.AutoField(primary_key=True)

    # Kategori alanı
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")

    # Ürün ismi
    name = models.CharField(max_length=200, verbose_name="Ürün İsmi")

    # Fiyat
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")

    # Oda sayısı
    room_count = models.PositiveIntegerField(verbose_name="Oda Sayısı", blank=True, null=True)

    # Banyo sayısı
    bathroom_count = models.PositiveIntegerField(verbose_name="Banyo Sayısı", blank=True, null=True)

    # Kat sayısı
    floor_count = models.PositiveIntegerField(verbose_name="Kat Sayısı", blank=True, null=True)

    # Metrekare
    square_meters = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Metrekare", blank=True, null=True)

    # Açıklama
    description = models.TextField(verbose_name="Açıklama", blank=True, null=True)

    # Otomatik olarak oluşturulma ve güncellenme tarihleri
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"


# Ürün resimleri için model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Ürün")
    image = models.ImageField(upload_to='product_images/', verbose_name="Resim")

    def __str__(self):
        return f"{self.product.name} Resim"

    class Meta:
        verbose_name = "Ürün Resmi"
        verbose_name_plural = "Ürün Resimleri"