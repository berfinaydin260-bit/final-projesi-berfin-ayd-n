import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import shap
import plotly.express as px

st.set_page_config(page_title="ChurnGuard AI", layout="wide")

@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("churn.csv")
    
    # Boşlukları ve hatalı metinleri sayısal veriye dönüştür
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
    df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
    
    # En anlamlı 5 sütunu seçiyoruz
    selected_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen', 'PaperlessBilling', 'Churn']
    df = df[selected_features]
    
    # 🚨 KRİTİK DÜZELTME: Veride kalan TÜM boş (NaN) değerleri kesin olarak temizle/sil
    df.dropna(inplace=True)
    
    # Kategorik verileri 1 ve 0'a dönüştür
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'Yes': 1, 'No': 0})
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Dönüşüm sonrası oluşabilecek olası boşlukları 0 ile doldur
    df.fillna(0, inplace=True)
    return df

df = load_and_clean_data()
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Random Forest (Rastgele Orman)": RandomForestClassifier(max_depth=5, random_state=42),
    "Logistic Regression (Lojistik Regresyon)": LogisticRegression(random_state=42)
}

model_results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    train_preds = model.predict(X_train)
    test_preds = model.predict(X_test)
    model_results[name] = {
        "Train Acc": accuracy_score(y_train, train_preds),
        "Test Acc": accuracy_score(y_test, test_preds),
        "Test F1": f1_score(y_test, test_preds),
        "object": model
    }

st.title("🛡️ ChurnGuard AI - Müşteri Terk Analizi Karar Destek Sistemi")
st.write("Bu yapay zekâ ürünü, müşterilerin şirketten ayrılma riskini tahmin eder.")
st.markdown("---")

st.sidebar.header("👤 Müşteri Değerlerini Girin")
tenure = st.sidebar.slider("Üyelik Süresi (Ay)", 1, 72, 12)
monthly_charges = st.sidebar.slider("Aylık Fatura ($)", 18, 120, 70)
total_charges = st.sidebar.slider("Toplam Ödenen Tutar ($)", 18, 8000, 840)
senior_citizen = st.sidebar.selectbox("Yaşlı Vatandaş Mı?", [0, 1], format_func=lambda x: "Evet" if x==1 else "Hayır")
paperless_billing = st.sidebar.selectbox("E-Fatura Kullanıyor Mu?", [1, 0], format_func=lambda x: "Evet" if x==1 else "Hayır")

selected_model = st.selectbox("📊 Kullanılacak Yapay Zekâ Modelini Seçin", list(models.keys()))
chosen_model = model_results[selected_model]["object"]

input_data = pd.DataFrame([{
    'tenure': tenure, 'MonthlyCharges': monthly_charges, 'TotalCharges': total_charges,
    'SeniorCitizen': senior_citizen, 'PaperlessBilling': paperless_billing
}])

st.subheader("🔮 Yapay Zekâ Tahmin Çıktısı")
col1, col2 = st.columns(2)

with col1:
    proba = chosen_model.predict_proba(input_data)[0][1]
    st.metric(label="Müşterinin Şirketi Bırakma (Terk) Riski", value=f"% {proba * 100:.1f}")
    
    if proba > 0.5:
        st.error("🚨 YÜKSEK RİSK: Bu müşteri şirketten ayrılma eğilimindedir!")
    else:
        st.success("✅ GÜVENLİ: Müşterinin bağlılık durumu yüksek.")

with col2:
    st.write("**Model Performans Sonuçları (Overfitting Analizi):**")
    st.json({
        "Eğitim Doğruluğu (Train Accuracy)": f"{model_results[selected_model]['Train Acc']:.2f}",
        "Test Doğruluğu (Test Accuracy)": f"{model_results[selected_model]['Test Acc']:.2f}"
    })

st.markdown("---")
st.subheader("💡 Yapay Zekâ Bu Kararı Neden Verdi? (SHAP Açıklaması)")

# 1. Eksik olan SHAP Hesaplama Motorunu Geri Ekliyoruz
explainer = shap.TreeExplainer(model_results["Random Forest (Rastgele Orman)"]["object"]) if "Random Forest" in selected_model else shap.LinearExplainer(model_results["Logistic Regression (Lojistik Regresyon)"]["object"], X_train)
shap_vals = explainer(input_data)

# 2. Boyut Hatasını Çözen Grafik Kısmı
if "Random Forest" in selected_model:
    sv = shap_vals.values[0][:, 1] if len(shap_vals.values[0].shape) == 2 else shap_vals.values[0]
else:
    sv = shap_vals.values[0]

fig = px.bar(
    x=sv,
    y=X.columns,
    orientation='h',
    labels={"x": "Riske Etki Boyutu (Sağa doğru risk artırır, Sola doğru azaltır)", "y": "Müşteri Özellikleri"},
    color=sv,
    color_continuous_scale=px.colors.sequential.RdBu_r
)
st.plotly_chart(fig, use_container_width=True)