---

```markdown
# Plagiarism Checker Python

Proyek ini adalah **tugas praktikum** yang bertujuan untuk membuat aplikasi sederhana pendeteksi plagiarisme menggunakan bahasa pemrograman Python.  
Aplikasi dapat membaca dokumen (PDF maupun teks), mengekstrak konten, lalu membandingkan kesamaan antar dokumen.

---

## 📂 Struktur Folder
- `app.py` → File utama untuk menjalankan aplikasi.
- `plagiarism_detector.py` → Modul inti untuk mendeteksi plagiarisme.
- `pdf_extractor.py` → Ekstraksi teks dari file PDF.
- `generate_docs.py` → Membuat dokumen contoh untuk pengujian.
- `sample_documents.py` → Contoh dokumen teks untuk uji coba.
- `documents/sample/` → Folder berisi dokumen sampel.
- `requirements.txt` → Daftar dependensi Python yang dibutuhkan.

---

## ⚙️ Instalasi
1. Clone repository:
   ```bash
   git clone https://github.com/wahyualvyy/plagiarism-checker-python.git
   cd plagiarism-checker-python
   ```

2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Cara Menjalankan
1. Pastikan dokumen yang ingin diperiksa ada di folder `documents/sample/`.
2. Jalankan aplikasi:
   ```bash
   python app.py
   ```
3. Program akan menampilkan hasil persentase kesamaan antar dokumen.

---

## 🧩 Fitur Utama
- Ekstraksi teks dari file PDF.
- Membandingkan isi antar dokumen teks.
- Menampilkan persentase kesamaan (indikasi plagiarisme).
- Mudah diperluas untuk format dokumen lain.

---

## 📌 Catatan
- Proyek ini dibuat untuk **keperluan praktikum** dan pembelajaran.
- Algoritma yang digunakan sederhana, sehingga hasil deteksi mungkin belum seakurat sistem profesional.
- Bisa dikembangkan lebih lanjut dengan algoritma NLP atau library seperti `scikit-learn`.

---

## 👨‍💻 Kontributor
- [wahyualvyy](https://github.com/wahyualvyy)

```

---