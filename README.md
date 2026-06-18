#  ChurnGuard AI - Açıklanabilir Müşteri Terk Analizi ve Karar Destek Sistemi

##  Projenin Adı
**ChurnGuard AI** - Yapay Zekâ Destekli Müşteri Terk Analizi ve Karar Destek Ürünü

##  Problem Tanımı
Şirketlerin hangi müşterilerinin hizmeti bırakacağını (churn) önceden tahmin edememesi ve klasik makine öğrenmesi modellerinin "neden bu tahmini yaptığını" açıklayamaması (kara kutu problemi). Bu durum, müşteri kayıplarını engellemek için doğru ve şeffaf aksiyonlar almayı zorlaştırmaktadır.

##  Hedef Kullanıcı
- Müşteri İlişkileri (CRM) Yöneticileri
- Pazarlama Stratejistleri
- Şirket Üst Düzey Yöneticileri

##  Çözümün Kısa Açıklaması
ChurnGuard AI, Kaggle üzerindeki gerçek müşteri verilerini kullanarak iki farklı makine öğrenmesi modeli eğitir. CRM uzmanının web arayüzünden girdiği müşteri bilgilerine dayanarak anlık terk riski hesaplar. En önemlisi, **SHAP (Explainable AI)** kütüphanesini entegre ederek yapay zekânın bu kararı hangi faktörlere (yüksek fatura, üyelik süresi vb.) dayanarak verdiğini grafiklerle şeffafça açıklar.

##  Kullanılan Teknolojiler
- Bu Ürünü yaparken geminiden yardım aldım.
- **Programlama Dili:** Python
- **Arayüz Geliştirme:** Streamlit
- **Yapay Zekâ ve Veri Bilimi:** Scikit-learn (Random Forest, Logistic Regression), SHAP (Açıklanabilir YZ)
- **Veri İşleme:** Pandas, Numpy
- **Veri Görselleştirme:** Plotly Express

##  Sistem Mimarisi ve İş Akışı
1. **Veri Girişi:** Kullanıcı web arayüzünden müşteri verilerini girer (Aylık ücret, kontrat süresi vb.).
2. **Model Motoru:** Arka planda eğitilmiş olan Random Forest ve Logistic Regression modelleri girdiyi işler.
3. **Tahmin ve Risk Skoru:** Model, müşterinin terk etme olasılıgini (%) hesaplar.
4. **XAI (SHAP) Analizi:** SHAP motoru çalışarak her özelliğin riske olan pozitif/negatif etkisini hesaplar.
5. **Görsel Çıktı:** Sonuçlar ve etki grafiği Streamlit arayüzünde kullanıcıya sunulur.

##  Kurulum Adımları
Uygulamayı yerelde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Bu depoyu bilgisayarınıza indirin.
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install streamlit pandas numpy scikit-learn shap plotly
   ## 📹 Tanıtım Videosu Linki
Geliştirilen ChurnGuard AI sisteminin canlı çalışma testini ve model performans analizlerini içeren tanıtım videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

👉 [Google Drive Tanıtım Videosu İzleme Linki](https://drive.google.com/file/d/1GqX8DcYAsfzgwlO97YVJulbLgmld4721/view?usp=drive_link)

