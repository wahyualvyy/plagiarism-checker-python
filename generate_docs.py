import os
import random

os.makedirs("documents/sample", exist_ok=True)

topics = {
    "plagiarisme": [
        "Plagiarisme akademik merupakan pelanggaran etika yang serius dalam dunia pendidikan tinggi.",
        "Tindakan plagiarisme dapat merugikan penulis asli serta menurunkan kualitas akademik.",
        "Perguruan tinggi menerapkan berbagai kebijakan untuk mencegah dan menindak plagiarisme.",
        "Deteksi plagiarisme penting untuk menjaga integritas dan orisinalitas karya ilmiah."
    ],
    "tfidf": [
        "TF-IDF merupakan metode pembobotan kata yang banyak digunakan dalam text mining.",
        "Metode ini menghitung frekuensi kemunculan kata dalam dokumen dan koleksi dokumen.",
        "TF-IDF membantu menentukan kata yang paling representatif dalam suatu dokumen.",
        "Dalam penelitian ini, TF-IDF digunakan untuk representasi fitur teks."
    ],
    "machine_learning": [
        "Machine learning adalah cabang kecerdasan buatan yang memungkinkan sistem belajar dari data.",
        "Algoritma machine learning banyak digunakan dalam klasifikasi dan prediksi data.",
        "Model machine learning memerlukan data latih yang cukup untuk menghasilkan performa optimal.",
        "Penerapan machine learning telah digunakan di berbagai bidang penelitian."
    ],
    "analisis_data": [
        "Analisis data bertujuan untuk menemukan pola dan informasi yang berguna.",
        "Proses analisis data melibatkan pengumpulan, pembersihan, dan pemodelan data.",
        "Hasil analisis data dapat digunakan sebagai dasar pengambilan keputusan.",
        "Analisis data banyak diterapkan dalam penelitian ilmiah dan industri."
    ],
    "sistem_informasi": [
        "Sistem informasi digunakan untuk mengelola data dan informasi dalam suatu organisasi.",
        "Pengembangan sistem informasi harus memperhatikan kebutuhan pengguna.",
        "Sistem informasi yang baik dapat meningkatkan efisiensi dan efektivitas kerja.",
        "Dalam penelitian ini dibahas perancangan sistem informasi berbasis komputer."
    ]
}

def generate_document(topic_sentences, doc_id):
    paragraphs = []
    for _ in range(4):
        paragraph = " ".join(random.sample(topic_sentences, k=3))
        paragraphs.append(paragraph)
    return "\n\n".join(paragraphs) + f"\n\nDokumen akademik ke-{doc_id}."

doc_id = 1
for topic, sentences in topics.items():
    for _ in range(10):  # 5 topik × 10 = 50 dokumen
        content = generate_document(sentences, doc_id)
        with open(f"documents/sample/doc{doc_id}.txt", "w", encoding="utf-8") as f:
            f.write(content)
        doc_id += 1

print("✅ 50 dokumen akademik realistis berhasil dibuat.")
