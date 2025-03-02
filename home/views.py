from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products,})


def contact(request):
    return render(request, 'contact.html')


def properties(request):
    filter_category = request.GET.get('category', 'all')

    if filter_category == 'all':
        properties = Product.objects.all()
    else:
        properties = Product.objects.filter(category__name__iexact=filter_category)  # Büyük-küçük harf duyarsız

    return render(request, 'properties.html', {'properties': properties})



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Ürünü veritabanından çek
    images = product.images.all()  # Ürünün resimlerini al

    return render(request, 'product_detail.html', {'product': product, 'images': images, })
