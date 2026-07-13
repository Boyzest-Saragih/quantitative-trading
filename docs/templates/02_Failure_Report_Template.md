# FAILURE REPORT

## Metadata
| Field | Value |
|-------|-------|
| Report ID | [FR-{H_ID}-{YYYYMMDD}] |
| Date Created | [YYYY-MM-DD] |
| Researcher | [Nama] |
| H_ID | [H001, H002, ...] |
| Phase | [Phase 3 - Statistical Validation] |
| Commit Hash | [Git commit hash] |
| Notebook Path | [QuantResearch/Notebook/...] |

---

## 1. WHAT FAILED
[Deskripsi spesifik apa yang gagal. Satu paragraf, jelas, tanpa alasan dulu.]

Contoh:
> Hipotesis H001 "Breakout setelah low volatility lebih profitable" ditolak. 
> Win rate 48% (threshold > 55%), profit factor 0.92. 
> Bootstrap confidence interval [0.42, 0.54] tidak mencakup threshold.

---

## 2. EVIDENCE

### 2.1 Metrics
| Metric | Value | Threshold | Pass? |
|--------|-------|-----------|-------|
| Win Rate | 0.48 | > 0.55 | ❌ |
| Profit Factor | 0.92 | > 1.0 | ❌ |
| Expected Value | -0.15 | > 0 | ❌ |
| P-Value | 0.34 | < 0.05 | ❌ |
| Sharpe Ratio | -0.22 | > 0 | ❌ |

### 2.2 Visual Evidence
[Grafik, distribusi, atau screenshot yang mendukung. Tempatkan di folder Reports/images/]

### 2.3 Log Output
```
[Copy relevant error log atau output dari notebook]
```

---

## 3. DIAGNOSIS CATEGORY

Pilih SATU yang paling dominan:

- [ ] **A. HYPOTHESIS WRONG** — Hipotesis tidak sesuai realitas market. Expected dan valid.
- [ ] **B. METHODOLOGY WRONG** — Cara pengujian salah (data leakage, wrong metric, etc.)
- [ ] **C. DATA INSUFFICIENT** — Sample size terlalu kecil atau periode tidak representatif.
- [ ] **D. OVERFIT** — Model/hipotesis terlalu spesifik ke data training.
- [ ] **E. DATA LEAKAGE** — Fitur menggunakan informasi masa depan. CRITICAL.
- [ ] **F. REGIME CHANGE** — Market structure berubah selama periode test.
- [ ] **G. EXECUTION GAP** — Real world execution tidak sesuai simulasi.
- [ ] **H. OTHER** — [Jelaskan]

**Selected:** [A/B/C/D/E/F/G/H]

**Justification:**
[Mengapa kategori ini? 3-5 kalimat dengan evidence.]

---

## 4. ROOT CAUSE ANALYSIS (5 Whys)

**Why 1:** Mengapa hipotesis gagal?
> [Jawaban]

**Why 2:** Mengapa [jawaban Why 1] terjadi?
> [Jawaban]

**Why 3:** Mengapa [jawaban Why 2] terjadi?
> [Jawaban]

**Why 4:** Mengapa [jawaban Why 3] terjadi?
> [Jawaban]

**Why 5:** Mengapa [jawaban Why 4] terjadi?
> [Root cause fundamental]

---

## 5. ACTION PLAN

### 5.1 Return To Phase
**Phase:** [Phase 2 - EDA / Phase 3 - Validation / Phase 4 - Feature / etc.]

**Alasan:** [Mengapa kembali ke phase ini?]

### 5.2 Specific Fix
- [ ] [Action item 1]
- [ ] [Action item 2]
- [ ] [Action item 3]

### 5.3 Re-test Criteria
[Apa yang harus terpenuhi agar dianggap "fixed"? Metrics spesifik.]

---

## 6. INSIGHT GAINED

[Apa yang saya pelajari dari kegagalan ini? Ini aset paling berharga.]

Contoh:
> "Low volatility tidak otomatis diikuti breakout. Seringnya konsolidasi berlanjut. 
> Breakout lebih mungkin terjadi setelah volume spike, bukan hanya low ATR."

---

## 7. NEXT EXPERIMENT

**H_ID Next:** [H007, H012, etc.]

**Hipotesis Next:**
> [Jika insight ini benar, maka hipotesis berikutnya adalah...]

**Expected Outcome:**
> [Measurable]

---

## 8. ATTACHMENTS

| File | Path | Description |
|------|------|-------------|
| Notebook | [path] | Eksperimen lengkap |
| Data | [path] | Dataset yang digunakan |
| Grafik | [path] | Visual evidence |
| Log | [path] | Output log |

---

## 9. SIGN-OFF

| | |
|---|---|
| Date Completed | [YYYY-MM-DD] |
| Reviewed By | [Self / Peer / Dosen] |
| Status | [CLOSED / PENDING REVISIT] |

---

> **"Menemukan bahwa sesuatu tidak bekerja adalah hasil yang valid. 
> Menghindari kegagalan yang didokumentasikan adalah menghindari kerugian yang lebih besar."**
