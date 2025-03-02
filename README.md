# RealEstate - Django Emlak Sitesi  

Bu proje, **Django** kullanılarak geliştirilmiş basit bir emlak sitesidir. Siteyi ücretsiz bir temayı kullanarak oluşturdum ve arka tarafını (backend) kendim kodladım.  

## 🚀 Özellikler  
- **Kategori Yönetimi**: Admin paneli üzerinden yeni emlak kategorileri ekleyebilirsiniz.  
- **Ürün (Emlak) Yönetimi**: Admin panelinde emlak ilanları ekleyebilir, düzenleyebilir ve silebilirsiniz.  
- **Modüler Yapı**: Siteyi **header, menu, slider** gibi parçalara böldüm ve `include` kullanarak ilgili bölümlere ekledim.  

## 🛠 Kullanılan Teknolojiler  
- **Django**: Backend geliştirme için  
- **Python**: Django ile kullanılan programlama dili  
- **SQLite**: Veritabanı yönetimi için  
- **HTML, CSS**: Ön yüz için (hazır tema kullanıldı)  

## 💻 Kurulum ve Çalıştırma  
Projeyi kendi bilgisayarınızda çalıştırmak için şu adımları takip edin:  

### 1️⃣ Gerekli Paketleri Yükleyin  
```bash
pip install django
```

### 2️⃣ Veritabanı Migrasyonlarını Yapın
```bash
python manage.py migrate
```

### 3️⃣ Admin Kullanıcısı
- **Kullanıcı Adı**: admin  
- **Şifre**: admin12345

Eğer farklı bir admin kullanıcısı oluşturmak isterseniz:
```bash
python manage.py createsuperuser
```

### 4️⃣ Projeyi Çalıştırın
```bash
python manage.py runserver
```

Ardından tarayıcınızda http://127.0.0.1:8000/ adresine giderek siteyi görüntüleyebilirsiniz.
Admin paneline giriş için http://127.0.0.1:8000/admin/ adresini kullanabilirsiniz.
