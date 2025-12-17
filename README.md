# 📘 Prediksi Efisiensi Energi Bangunan Menggunakan Machine Learning dan Deep Learning

## 👤 Informasi
- **Nama:** Ergi Zenila Marta Sasmige  
- **NIM:** 233307010  
- **Program Studi:** Teknologi Informasi  
- **Mata Kuliah:** Data Science  
- **Dosen Pengampu:** Gus Nanang Syaifuddiin  
- **Repository:** https://github.com/ezms1735/UAS_DataScience.git
- **Video Presentasi:** https://drive.google.com/file/d/1CFZO0pL03sq113fp7VaSmOXzUZrHiKU8/view?usp=sharing 

---

## 🎯 1. Ringkasan Proyek
Proyek ini bertujuan untuk **memprediksi efisiensi energi bangunan** menggunakan *Energy Efficiency Dataset* dari UCI Machine Learning Repository.  
Fokus utama adalah memprediksi **Heating Load** berdasarkan parameter fisik bangunan seperti luas permukaan, tinggi, orientasi, dan area kaca.  

Tahapan utama yang dilakukan:
- Analisis dan eksplorasi data (EDA)  
- Data preprocessing dan normalisasi  
- Pembangunan tiga model pembelajaran:
  - **Baseline:** Linear Regression  
  - **Advanced ML:** Random Forest Regressor  
  - **Deep Learning:** Multilayer Perceptron (MLP)
- Evaluasi model menggunakan metrik regresi  
- Penentuan model terbaik berdasarkan performa  

---

## 📄 2. Problem & Goals

### **Problem Statements**
- Bagaimana cara memprediksi kebutuhan energi pemanasan pada bangunan berdasarkan parameter fisiknya?  
- Bagaimana performa model machine learning dan deep learning dalam mempelajari hubungan non-linear antar fitur?  
- Model mana yang paling akurat dan efisien dalam memprediksi Heating Load?

### **Goals**
- Membangun model prediksi efisiensi energi dengan akurasi tinggi (**R² > 0.90**).  
- Membandingkan performa tiga pendekatan model (Baseline, Advanced ML, Deep Learning).  
- Menentukan model terbaik berdasarkan metrik **MAE, MSE, RMSE, dan R² Score**.  
- Menyediakan sistem prediksi yang dapat direproduksi dengan struktur proyek yang terorganisir.  

---

## 📁 3. Struktur Folder
```
energy-efficiency-prediction/
│
├── data/ # Dataset (tidak di-commit)
│ └── Energy Efficency_data.xlsx
│
├── notebooks/ # Notebook utama proyek
│ └── EnergyEfficiency_Project.ipynb
│
├── src/ # Script modular
│
├── models/ # Model yang disimpan
│ ├── model_lr.pkl
│ ├── model_mlp.h5
│ └── model_rf.pkl
│
├── images/ # Visualisasi hasil analisis
│ ├── cek_outlier.png
│ ├── deep_learning.png
│ ├── heatmadp_korelasi.png
│ ├── linear_regression.png
│ ├── perbandingan_mae.png
│ ├── perbandingan_r2.png
│ ├── prediksi_error_mlp.png
│ ├── random_forest_regressor.png
│ ├── training_validation_loss.png
│ ├── training_validation_mae.png
│ ├── visualisasi_1.png
│ ├── visualisasi_2.png
│ ├── visualisasi_3.png
│ ├── visualisasi_distribusi.png
│
├── requirements.txt # Daftar dependencies
├── .gitignore
└── README.md
```

---

## 📊 4. Dataset
- **Sumber:** [UCI Machine Learning Repository – Energy Efficiency Dataset](https://archive.ics.uci.edu/dataset/242/energy+efficiency)  
- **Jumlah data:** 768 baris × 10 kolom  
- **Tipe data:** Tabular (numerik)  
- **Format:** `.xlsx` / `.csv`  

### **Deskripsi Fitur**
| Fitur | Deskripsi |
|-------|------------|
| Relative Compactness | Tingkat kekompakan bentuk bangunan |
| Surface Area | Luas total permukaan bangunan (m²) |
| Wall Area | Luas dinding bangunan (m²) |
| Roof Area | Luas atap bangunan (m²) |
| Overall Height | Tinggi bangunan (m) |
| Orientation | Arah orientasi bangunan (1–4) |
| Glazing Area | Luas area kaca (proporsi) |
| Glazing Area Distribution | Distribusi area kaca (0–5) |
| Heating Load | Kebutuhan energi untuk pemanasan (kWh/m²) |
| Cooling Load | Kebutuhan energi untuk pendinginan (kWh/m²) |

---

## 🔧 5. Data Preparation

Langkah-langkah:
- **Data Cleaning:** Tidak ditemukan missing values atau duplikasi data.  
- **Feature Scaling:** Normalisasi menggunakan `StandardScaler`.  
- **Data Splitting:** Pembagian data menjadi 80% train dan 20% test (random_state=42).  
- **Balancing:** Tidak diperlukan karena target bersifat kontinu (regresi).  

---

## 🤖 6. Modeling

### **Model 1 – Baseline**
**Linear Regression**
- Sederhana dan efisien untuk memodelkan hubungan linear antar fitur.  
- Digunakan sebagai acuan awal sebelum mencoba model kompleks.

### **Model 2 – Advanced ML**
**Random Forest Regressor**
- Menangkap hubungan non-linear antar fitur.  
- Parameter utama:
  - n_estimators = 100  
  - max_depth = 10  
  - random_state = 42  

### **Model 3 – Deep Learning**
**Multilayer Perceptron (MLP)**
- Arsitektur:
  - Dense(128, ReLU)  
  - Dropout(0.3)  
  - Dense(64, ReLU)  
  - Dropout(0.3)  
  - Dense(1, Linear)
- Optimizer: Adam  
- Loss Function: MSE  
- Epochs: 50  
- Batch Size: 32  
- Validation Split: 0.2  

---

## 🧪 7. Evaluation

### **Metrik yang Digunakan**
- MAE (Mean Absolute Error)  
- MSE (Mean Squared Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

### **Hasil Evaluasi**
| Model | MAE | MSE | RMSE | R² |
|--------|-----|-----|------|----|
| Linear Regression | 2.10 | 8.40 | 2.90 | 0.89 |
| Random Forest | 1.20 | 4.10 | 2.02 | 0.96 |
| MLP (Deep Learning) | 1.05 | 3.60 | 1.90 | 0.97 |

📈 Visualisasi Perbandingan:  
- Disimpan di `images/model_comparison.png`  
- Grafik Loss/Accuracy pada `images/training_loss_accuracy.png`  

---

## 🏁 8. Kesimpulan

- **Model Terbaik:** Multilayer Perceptron (MLP)  
- **Performa:**  
  - R² = **0.97**  
  - RMSE = **1.90**  
  - MAE = **1.05**  

**Insight:**
- Fitur *Relative Compactness* paling berpengaruh terhadap efisiensi energi.  
- Model *Deep Learning (MLP)* menunjukkan performa terbaik dibandingkan model linear dan tree-based.  
- Dataset dengan pola non-linear lebih cocok dimodelkan menggunakan pendekatan neural network.  

---

## 🔮 9. Future Work
- [✅] Tambah variasi dan jumlah data  
- [✅] Melakukan hyperparameter tuning lebih lanjut  
- [✅] Mencoba arsitektur deep learning lain (Autoencoder / CNN1D)  
- [✅] Deploy model menggunakan Streamlit atau Flask untuk tampilan web interaktif  

---

## 🔁 10. Reproducibility

### **Environment**
```bash
python -m venv venv
venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt
