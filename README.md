```markdown
# Plagiarism Checker Python

Proyek ini merupakan **tugas praktikum/penugasan individu** untuk membangun aplikasi pendeteksi plagiarisme dokumen akademik berbahasa Indonesia menggunakan metode **TF-IDF** dan **Cosine Similarity**.  
Aplikasi dibuat menggunakan bahasa pemrograman **Python** dan antarmuka berbasis web dengan **Streamlit**.

---

## 📂 Struktur Folder

```

plagiarism-checker-python/
├── app.py
├── plagiarism_detector.py
├── pdf_extractor.py
├── sample_documents.py
├── generate_academic_docs.py
├── requirements.txt
├── README.md
└── documents/
├── sample/
│   └── doc1.txt ... doc50.txt
└── uploads/

```

---

## ⚙️ Instalasi

1. Pastikan Python versi 3.8 atau lebih baru sudah terpasang:
```

python --version

```

2. (Opsional) Buat virtual environment:
```

python -m venv venv
venv\Scripts\activate

```

3. Install seluruh dependensi:
```

pip install -r requirements.txt

```

---

## 📄 Menyiapkan Dokumen Referensi

Untuk membuat minimal 50 dokumen referensi secara otomatis, jalankan:
```

python generate_academic_docs.py

```

Dokumen referensi akan tersimpan di folder:
```

documents/sample/

```

---

## ▶️ Cara Menjalankan Aplikasi

Jalankan aplikasi dengan perintah:
```

python -m streamlit run app.py

```

Aplikasi akan terbuka di browser melalui alamat:
```

[http://localhost:8501](http://localhost:8501)

```

---

## 🧪 Cara Menggunakan Aplikasi

1. Buka aplikasi di browser.
2. Upload satu dokumen berformat `.txt` atau `.pdf`.
3. Atur nilai threshold similarity (default 0.7).
4. Tunggu proses deteksi selesai.
5. Hasil yang ditampilkan:
   - Daftar dokumen dengan similarity di atas threshold
   - Highlight bagian teks yang mirip
   - Similarity matrix (heatmap)
   - Statistik hasil deteksi

Dokumen yang diunggah akan otomatis disimpan di:
```

documents/uploads/

```

---

## 🧩 Fitur Utama
- Ekstraksi teks dari file PDF dan TXT
- Deteksi plagiarisme menggunakan TF-IDF dan cosine similarity
- Filtering dokumen berdasarkan threshold
- Highlight bagian teks yang mirip
- Visualisasi similarity matrix
- Statistik hasil deteksi

---

## 📌 Catatan
- File PDF harus berupa **PDF berbasis teks**, bukan hasil scan gambar.
- Sistem ini dibuat untuk **keperluan akademik dan pembelajaran**.
- Hasil deteksi bersifat indikatif dan bukan pengganti sistem profesional.

---

## 👨‍💻 Kontributor
- wahyualvyy
```
