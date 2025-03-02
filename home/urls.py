from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('properties', views.properties, name='properties'),
    path('property/<int:product_id>/', views.product_detail, name='product_detail'),

]

# MEDIA dosyalarına erişim için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
