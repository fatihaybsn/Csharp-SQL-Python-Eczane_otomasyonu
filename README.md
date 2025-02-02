# Eczane Otomasyonu - README

Merhaba,  
Ben [Adınız Soyadınız], bir Bilgisayar Mühendisliği öğrencisi olarak geliştirmiş olduğum Eczane Otomasyonu projesini sizlerle paylaşmaktan memnuniyet duyuyorum. Proje, C#, MsSQL ve Python dillerinin gücünü bir araya getirerek, modern, entegre ve verimli bir eczane otomasyonu çözümü sunmaktadır.

---

## İçindekiler
- [Genel Bakış](#genel-bakış)
- [Teknoloji ve Diller](#teknoloji-ve-diller)
- [Sistem Mimarisi ve Özellikler](#sistem-mimarisi-ve-özellikler)
  - [Entegre Sistemler](#entegrasyon-sistemleri)
  - [Python ile Gerçek Zamanlı Barkod Okuma](#python-ile-gerçek-zamanlı-barkod-okuma)
  - [Doktor Modülü](#doktor-modülü)
  - [Eczane Modülü](#eczane-modülü)
- [Veritabanı Tasarımı ve İşlevleri](#veritabanı-tasarımı-ve-işlevleri)
  - [Tablolar ve Veri Setleri](#tablolar-ve-veri-setleri)
  - [Trigger, View, Store Procedure ve Fonksiyonlar](#trigger-view-store-procedure-ve-fonksiyonlar)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Sonuç ve Yorumlar](#sonuç-ve-yorumlar)

---

## Genel Bakış
Bu proje, modern eczane otomasyon sistemlerinin gereksinimlerini karşılamak üzere tasarlanmıştır. Üç temel kullanıcı tipi (Hasta, Doktor, Eczane) için entegre modüller sunarak, her bir sistemin kendi işlevselliğini korurken, aralarındaki veri alışverişini de sağlamaktadır. Proje, kullanıcı dostu arayüzü, gerçek zamanlı veri işleme kabiliyeti ve sağlam veritabanı yapısı ile öne çıkmaktadır.

---

## Teknoloji ve Diller
Proje geliştirilirken aşağıdaki teknolojiler kullanılmıştır:
- **C#**: Ana uygulama mantığının ve arayüzünün geliştirilmesinde kullanılmıştır. C# ile yazılmış exe dosyası, sistemin çekirdeğini oluşturmaktadır.
- **MsSQL**: Veritabanı yönetim sistemi olarak tercih edilmiştir. Tablolar, trigger, view, store procedure ve fonksiyonlar ile veri tutarlılığı ve performans artırılmıştır.
- **Python**: Barkod okuma işlemleri için entegre edilmiş olup, kamera aracılığıyla barkod verilerini okuyarak C# uygulamasına anlık veri aktarımını sağlamaktadır.

---

## Sistem Mimarisi ve Özellikler

### Entegre Sistemler
Proje üç ana modülü entegre etmektedir:
- **Hasta Girişi**: Hastaların randevu, reçete ve diğer tıbbi bilgilerinin yönetimi.
- **Doktor Girişi**: Doktorların reçete oluşturma, düzenleme, muayene ekleme, raporlama ve kullanıcı işlemleri gibi geniş fonksiyonlara sahip modül.
- **Eczane Girişi**: Eczane personelinin, yazılan ereçeteleri görüntüleme, kağıt reçete girişi, reçetesiz ilaç satışı, stok durumunu sorgulama ve barkod okuma entegrasyonunu kullanarak ilaç sorgulama işlemlerinin yürütülmesi.

### Python ile Gerçek Zamanlı Barkod Okuma
Benzersiz bir entegrasyon ile Python tabanlı barkod okuma sistemi, C# uygulamasıyla kesintisiz veri alışverişi gerçekleştirmektedir.  
- **Nasıl Çalışır?**  
  Python, kamera aracılığıyla barkod verilerini okur ve bu bilgileri C# uygulamasına aktarır. Bu sayede eczane modülü, anında ilacın stok ve diğer bilgilerini sorgulayarak kullanıcıya hızlı sonuç sunar.
- **Avantajları:**  
  - Gerçek zamanlı veri aktarımı ve işleme.
  - Kullanıcı deneyiminde kesintisiz ve hızlı işlem akışı.
  - İki farklı programlama dilinin entegrasyonu ile çok yönlü çözümler.

### Doktor Modülü
Doktor kullanıcıları için geliştirilen modül;  
- Ereçete ekleme ve silme.
- Rapor oluşturma.
- Muayene ekleme.
- Kapsamlı kullanıcı işlemleri yapabilme imkanı sunar.  
Bu modül, tıbbi veri girişinde ve yönetiminde yüksek doğruluk ve performans sağlamak üzere optimize edilmiştir.

### Eczane Modülü
Eczane çalışanları, sistemde şu işlemleri gerçekleştirebilir:
- Yazılan ereçeteyi görme ve reçete girişi yapma.
- Kağıt reçete girme.
- Reçetesiz ilaç satışı.
- Barkod okuma sayesinde ilacın stok durumunu hızlıca sorgulama.  
Barkod entegrasyonu sayesinde, ilaç sorgulama süreci büyük oranda otomatikleştirilmiş ve hatasız hale getirilmiştir.

---

## Veritabanı Tasarımı ve İşlevleri

### Tablolar ve Veri Setleri
- **Toplam 13 Tablo:** Proje kapsamında, kullanıcı, reçete, ilaç ve stok yönetimi gibi işlemleri destekleyen 13 farklı tablo bulunmaktadır.
- **İlaç Tablosu:** 7000'den fazla ilaç verisini barındıran ve 14 sütundan oluşan geniş kapsamlı bir veri tablosudur. Bu tablo, sistemin temel yapı taşlarından biri olarak, ilaç sorgulama ve stok yönetiminde kritik rol oynar.

### Trigger, View, Store Procedure ve Fonksiyonlar
- **Trigger:**  
  - Fatura oluşturulması, veritabanı düzeyinde bir trigger (TRG) ile otomatikleştirilmiştir. Bu sayede, her reçete satışında anında fatura kaydı oluşturulur.
- **View:**  
  - Reçete ve ereçete bilgilerini bir araya getiren 2 adet view ile verilerin kullanıcıya daha okunabilir ve düzenli sunumu sağlanmıştır.
- **Store Procedure:**  
  - Arama işlemleri (ilaç, hasta, doktor vb.) için 11 adet önceden derlenmiş store procedure kullanılarak, sorgu işlemlerinin hızlandırılması ve veritabanı performansının artırılması hedeflenmiştir.
- **Fonksiyonlar:**  
  - Oluşturulan reçete ve fatura numaralarının benzersizliğini kontrol etmek amacıyla 3 adet fonksiyon geliştirilmiştir.

Bu yapı, sistemin hem performansını artırmakta hem de veri bütünlüğünü sağlamaktadır.

---

## Kurulum ve Çalıştırma

1. **Dosya Dağıtımı:**  
   Proje, exe dosyası ve yanındaki `.bak` uzantılı veritabanı yedeği ile dağıtılmaktadır.

2. **Veritabanı Kurulumu:**  
   - Sağlanan `.bak` dosyasını, MsSQL Server Management Studio (SSMS) kullanarak restore (geri yükleme) işlemi ile veritabanınıza aktarınız.
   - Restore işleminde, veritabanı dosyasının yerini ve bağlantı ayarlarınızı doğru yapılandırdığınızdan emin olunuz.

3. **Uygulama Çalıştırma:**  
   - Restore işlemi tamamlandıktan sonra, exe dosyasını çalıştırarak sistemin tüm özelliklerine erişebilirsiniz.
   - Uygulama içerisinde kullanıcı tipi seçimi yaparak, Hasta, Doktor veya Eczane modüllerine giriş yapabilirsiniz.

---

## Sonuç ve Yorumlar
Bu eczane otomasyonu projesi, modern yazılım geliştirme tekniklerinin ve entegrasyon çözümlerinin başarılı bir örneğidir.  
- **Entegrasyon Başarısı:** C# ve Python'un kesintisiz veri alışverişi yapabilmesi, sistemin esnekliğini ve hızını artırmaktadır.
- **Veritabanı Performansı:** Trigger, view, store procedure ve fonksiyon kullanımı ile veritabanı işlemleri optimize edilmiş ve yüksek performans sağlanmıştır.
- **Modüler Yaklaşım:** Hasta, Doktor ve Eczane modüllerinin ayrı ayrı yönetilebilmesi, sistem bakım ve güncellemelerinde büyük kolaylık sağlamaktadır.

Projemi geliştirirken edindiğim deneyimleri ve karşılaştığım zorlukları, bu README ile özetlemeye çalıştım. Geri bildirimleriniz ve önerileriniz, projemi daha da geliştirmek için büyük önem taşımaktadır.

---

Teşekkürler,  
[Adınız Soyadınız]  
Bilgisayar Mühendisliği Öğrencisi  
(İletişim Bilgileriniz)

--- 

*Bu proje, akademik çalışmalar ve profesyonel uygulamalar arasında köprü kurmayı hedefleyerek, modern yazılım mühendisliği prensiplerini yansıtmaktadır.*
