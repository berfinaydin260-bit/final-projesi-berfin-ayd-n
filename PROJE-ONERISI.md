# PROJE ÖNERİSİ

- **Seçilen Görev Numarası:** Seçenek 3 (Açıklanabilir Makine Öğrenmesi Karar Destek Ürünü)
- **Ürünün Adı:** ChurnGuard AI - Yapay Zekâ Destekli Müşteri Terk Analizi ve Karar Destek Sistemi
- **Çözülecek Problem:** Şirketlerin (Telekom/Banka/E-ticaret) hangi müşterilerinin hizmeti bırakacağını önceden tahmin edememesi ve klasik makine öğrenmesi modellerinin "neden bu tahmini yaptığını" açıklayamaması. Bu durum, müşteri kayıplarını engellemek için doğru aksiyon almayı zorlaştırmaktadır.
- **Hedef Kullanıcı:** Müşteri İlişkileri Yöneticileri, Pazarlama Stratejistleri ve Şirket Yöneticileri.
- **Kullanılacak Veri Kaynakları:** Kaggle üzerinde yer alan, müşterilerin üyelik süreleri, aylık ödemeleri, şikayet sayıları ve hizmet kullanım detaylarını içeren açık erişimli "Telco Customer Churn" veri seti.
- **Kullanılması Planlanan Teknolojiler:** Python, Scikit-learn (Model Eğitimi), SHAP (Açıklanabilir Yapay Zekâ), Streamlit (Web Arayüzü), Pandas & Numpy (Veri Önişleme), Plotly (Grafikler).
- **Beklenen Ürün Çıktısı:** CRM uzmanının bir müşterinin bilgilerini girdiğinde sistemin o müşterinin terk etme riskini (%) hesapladığı ve SHAP grafikleriyle bu riskin arkasındaki temel nedenleri (örneğin: "Son 3 aydaki yüksek şikayet sayısı riski %40 artırdı") dinamik olarak gösterdiği çalışan bir web uygulaması.
- **Ürünün Diğer Çalışmalardan Ayrılan Yönü:** Sadece kuru bir risk tahmini üretmekle kalmayıp, XAI (Açıklanabilir Yapay Zekâ) teknikleriyle her müşteri özelinde terk eğilimini tetikleyen kök nedenleri şeffafça ortaya koyması ve yöneticilere doğrudan aksiyon alabilecekleri bir karar desteği sunması.
