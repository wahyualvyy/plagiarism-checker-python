import os
import wikipedia # type: ignore
import random
import time

# Konfigurasi Folder
output_dir = "documents/sample"
os.makedirs(output_dir, exist_ok=True)

# Konfigurasi Wikipedia ke Bahasa Indonesia
wikipedia.set_lang("id")

# Daftar Topik Akademik Nyata untuk Pencarian
# Kita siapkan lebih dari 50 topik untuk cadangan jika ada yang gagal diload
academic_keywords = [
    # Ilmu Komputer & Teknologi
    "Kecerdasan buatan", "Pembelajaran mesin", "Pengolahan bahasa alami", "Visi komputer", 
    "Sistem pakar", "Komputasi awan", "Internet of Things", "Keamanan jaringan", 
    "Blockchain", "Big data", "Sistem informasi", "Basis data", "Algoritma genetika",
    
    # Ekonomi & Bisnis
    "Makroekonomi", "Mikroekonomi", "Manajemen pemasaran", "Akuntansi keuangan", 
    "Perdagangan internasional", "Saham", "Investasi", "Kewirausahaan", "Manajemen risiko",
    
    # Kesehatan & Kedokteran
    "Epidemiologi", "Imunologi", "Farmakologi", "Genetika", "Kanker", "Diabetes melitus", 
    "Kesehatan masyarakat", "Gizi", "Psikologi klinis", "Neurobiologi",
    
    # Teknik
    "Teknik sipil", "Teknik elektro", "Energi terbarukan", "Robotika", "Termodinamika", 
    "Mekanika fluida", "Teknik industri", "Material komposit",
    
    # Hukum & Sosial
    "Hukum pidana", "Hukum perdata", "Sosiologi", "Antropologi", "Hubungan internasional", 
    "Politik", "Komunikasi massa", "Jurnalistik", "Hak asasi manusia"
]

def fetch_and_save_real_data(keywords, limit=50):
    count = 0
    used_keywords = []
    
    print(f"🔄 Memulai proses pengunduhan {limit} dokumen referensi dari Wikipedia...")
    
    # Acak urutan keyword agar variatif setiap kali dijalankan
    random.shuffle(keywords)

    for keyword in keywords:
        if count >= limit:
            break
            
        try:
            # Mengambil halaman wikipedia
            # auto_suggest=False agar tidak mengambil halaman yang salah
            page = wikipedia.page(keyword, auto_suggest=False)
            
            # Mengambil konten (Ringkasan + Isi)
            # Kita batasi karakternya agar tidak terlalu panjang (misal 3000-5000 karakter)
            content = page.content[:5000] 
            
            # Membersihkan sedikit format jika ada header yang tertinggal
            clean_content = f"Judul: {page.title}\nSumber: Wikipedia Indonesia\n\n{content}"
            
            # Simpan ke file
            filename = f"doc{count+1}_{keyword.replace(' ', '_')}.txt"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(clean_content)
            
            print(f"✅ [{count+1}/{limit}] Berhasil mengunduh: {page.title}")
            count += 1
            used_keywords.append(keyword)
            
        except wikipedia.exceptions.DisambiguationError as e:
            # Jika kata kunci ambigu, lewati
            print(f"⚠️ Ambigu: {keyword} (Dilewati)")
            continue
        except wikipedia.exceptions.PageError:
            # Jika halaman tidak ditemukan
            print(f"❌ Tidak ditemukan: {keyword}")
            continue
        except Exception as e:
            print(f"❌ Error pada {keyword}: {e}")
            continue

    print(f"\n🎉 Selesai! {count} dokumen berhasil disimpan di folder '{output_dir}'.")

# Jalankan Fungsi
if __name__ == "__main__":
    fetch_and_save_real_data(academic_keywords, limit=50)