# app.py
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

from plagiarism_detector import PlagiarismDetector
from pdf_extractor import read_document
from sample_documents import load_reference_documents

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Plagiarism Checker Indonesia",
    layout="wide"
)

st.title("📚 Plagiarism Checker Dokumen Akademik")
st.write("Deteksi plagiarisme menggunakan **TF-IDF & Cosine Similarity**")

# ======================
# FOLDER PATH
# ======================
REF_FOLDER = "documents/sample"
UPLOAD_FOLDER = "documents/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ======================
# LOAD DATABASE
# ======================
reference_docs = load_reference_documents(REF_FOLDER)
st.sidebar.success(f"📂 {len(reference_docs)} dokumen referensi dimuat")

# ======================
# UPLOAD DOKUMEN BARU
# ======================
uploaded_file = st.file_uploader(
    "📄 Upload dokumen (.pdf / .txt)",
    type=["pdf", "txt"]
)

threshold = st.slider(
    "🔧 Threshold Similarity",
    min_value=0.1,
    max_value=0.95,
    value=0.7,
    step=0.05
)

if uploaded_file is not None:
    # ======================
    # SIMPAN FILE KE documents/uploads
    # ======================
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # ======================
    # BACA DOKUMEN
    # ======================
    new_doc_text = read_document(file_path)

    detector = PlagiarismDetector()

    new_doc = {
        "name": uploaded_file.name,
        "content": new_doc_text
    }

    with st.spinner("🔍 Mengecek plagiarisme..."):
        result = detector.detect_plagiarism(
            new_doc,
            reference_docs,
            threshold=threshold
        )

    # ======================
    # HASIL UTAMA
    # ======================
    st.subheader("📊 Hasil Deteksi")

    df_results = pd.DataFrame(result["results"])
    df_results["Similarity (%)"] = (df_results["similarity"] * 100).round(2)
    df_results["Status"] = df_results["similarity"].apply(
        lambda x: "PLAGIARISME" if x >= threshold else "AMAN"
    )

    filtered = df_results[df_results["similarity"] >= threshold]

    if not filtered.empty:
        st.dataframe(
            filtered[["doc_name", "Similarity (%)", "Status"]]
        )
    else:
        st.info("Tidak ada dokumen dengan similarity di atas threshold")

    # ======================
    # DOKUMEN TERDETEKSI
    # ======================
    st.subheader("🚨 Dokumen Melebihi Threshold")

    if result["plagiarized"]:
        for doc in result["plagiarized"]:
            st.markdown(f"### 📄 {doc['doc_name']}")
            st.write(f"**Similarity:** `{doc['similarity']:.3f}`")

            if doc["matched_phrases"]:
                st.markdown("### 🔎 Bagian Teks Mirip")
                highlighted = detector.highlight_text(
                    new_doc["content"],
                    doc["matched_phrases"]
                )
                st.markdown(highlighted)
    else:
        st.success("✅ Tidak ada plagiarisme terdeteksi")

    # ======================
    # VISUALISASI MATRIX
    # ======================
    st.subheader("📈 Similarity Matrix")

    sim_values = np.array(result["similarity_matrix"]).reshape(1, -1)

    fig, ax = plt.subplots(figsize=(12, 2))
    sns.heatmap(
        sim_values,
        cmap="Reds",
        xticklabels=[doc["name"] for doc in reference_docs],
        yticklabels=["Dokumen Baru"],
        ax=ax
    )
    plt.xticks(rotation=90)
    st.pyplot(fig)

    # ======================
    # STATISTIK
    # ======================
    st.subheader("📌 Statistik")
    st.json(result["stats"])
