# 📈 Quantitative Trading Engine with Machine Learning

Sebuah *framework quantitative trading* mandiri yang dibangun untuk melakukan analisis prediktif pada pasar keuangan menggunakan Machine Learning (bukan LLM API wrapper). Project ini mengintegrasikan pemodelan statistik, *machine learning regression*, serta infrastruktur *backtesting* kustom untuk menciptakan strategi trading yang objektif dan terukur.

---

## 🎯 Project Goals & Core Architecture
Project ini fokus pada penerapan sains data murni ke dalam market keuangan dengan pilar utama:
* **True Machine Learning Integration:** Menggunakan algoritma **Ridge Regression** dan **Random Forest** sebagai *predictive engine* utama.
* **Hybrid Approach:** Mengombinasikan kekuatan *statistical forecasting* (analisis deret waktu/ekonometrika) dengan fleksibilitas model ML.
* **Zero Third-Party Bias:** Membangun *backtester* sendiri dari nol untuk memastikan transparansi metrik, eksekusi order, dan perhitungan *slippage/fee* yang akurat.

---

## 🚀 Roadmap & Milestones

### Phase 1: Data Infrastructure & Baseline
* [ ] **Historical Data Harvesting:** Mengumpulkan dan membersihkan data historis berkualitas tinggi untuk 1 target *currency pair*.
* [ ] **Custom Backtester Engine:** Membangun simulator *backtesting* mandiri yang objektif tanpa bergantung pada *library* pihak ketiga yang *black-box*.
* [ ] **Rule-Based Benchmark:** Menyusun strategi berbasis aturan (*rule-based*) simpel sebagai *baseline* untuk mengukur performa objektif sebelum model ML diterapkan.

### Phase 2: Feature Engineering & ML Modeling
* [ ] **Advanced Feature Engineering:** Eksplorasi indikator teknikal, transformasi statistik, volatilitas, dan fitur lag untuk menangkap *alpha*.
* [ ] **Model Training & Selection:** Mengimplementasikan model Ridge Regression (untuk menangani multikolinieritas) dan Random Forest (untuk menangkap hubungan non-linear).

### Phase 3: Validation & Live Execution
* [ ] **Walk-Forward Testing:** Menerapkan validasi *walk-forward* yang ketat (bukan *single-period backtest*) guna meminimalkan risiko *overfitting* dan *data leakage*.
* [ ] **MT5 Integration:** Menghubungkan *engine* ke MetaTrader 5 (MT5) API untuk kebutuhan *forward testing / paper trading* secara *real-time*.

---

## 🔬 The Ultimate Challenge: Researching
Tantangan terbesar dari project ini bukanlah menulis kodenya, melainkan **Proses Riset**. Menemukan *features* yang memiliki daya prediksi kuat, menjinakkan *noise* di market, serta memastikan model tetap tangguh saat menghadapi perubahan rezim pasar (*market regime shifts*) adalah fokus riset utama dalam repositori ini.

---

## 🛠️ Tech Stack (Planned)
* **Language:** Python
* **Data & ML:** Pandas, NumPy, Scikit-Learn, Statsmodels
* **Execution:** MetaTrader 5 Python API