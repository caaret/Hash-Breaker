# ⚡ Hash-Breaker v1.0
**Hash-Breaker**, Python ile geliştirilmiş, asenkron mantığına yakın çalışan ve hash türünü otomatik tespit edebilen bir Brute-Force şifre kırıcıdır.

### 🔥 Özellikler
- **Otomatik Hash Tespiti:** Girilen hash'in uzunluğuna göre MD5, SHA-1, SHA-256 gibi türleri otomatik tanır.
- **Kapsamlı Brute-Force:** `itertools` kullanarak matematiksel olarak tüm kombinasyonları dener.
- **Renkli Arayüz:** `colorama` desteği ile hata ve başarı durumlarını görselleştirir.
- **Geniş Algoritma Desteği:** MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.

### 🛠️ Kurulum
```bash
# Projeyi indirin
git clone [https://github.com/caaret/Hash-Breaker.git](https://github.com/caaret/Hash-Breaker.git)

# Gerekli kütüphaneyi yükleyin
pip install colorama