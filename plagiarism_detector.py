import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PlagiarismDetector:
    def __init__(self, stopwords=None):
        """
        Inisialisasi Plagiarism Detector
        
        Args:
            stopwords: List stopwords bahasa Indonesia
        """
        if stopwords is None:
            self.stopwords = self.get_indonesian_stopwords()
        else:
            self.stopwords = stopwords
        
        self.vectorizer = TfidfVectorizer(
            stop_words=self.stopwords,
            lowercase=True,
            token_pattern=r'\b[a-zA-Z]{3,}\b',  # Minimal 3 huruf
            ngram_range=(1, 2)  # Unigram dan bigram
        )
    
    @staticmethod
    def get_indonesian_stopwords():
        """
        Daftar stopwords bahasa Indonesia
        """
        return [
            'yang', 'dan', 'di', 'dari', 'ke', 'pada', 'untuk', 'adalah',
            'dengan', 'dalam', 'ini', 'itu', 'atau', 'akan', 'oleh', 'telah',
            'juga', 'sebagai', 'dapat', 'lebih', 'tidak', 'ada', 'sudah',
            'satu', 'dua', 'tiga', 'bisa', 'serta', 'antara', 'tersebut',
            'sangat', 'karena', 'hingga', 'melalui', 'terhadap', 'harus',
            'mereka', 'sama', 'setiap', 'seperti', 'semua', 'namun', 'masih',
            'saat', 'hanya', 'kini', 'pula', 'bila', 'maka', 'ia', 'kami'
        ]
    
    def preprocess_text(self, text):
        """
        Preprocessing teks
        """
        # Lowercase
        text = text.lower()
        # Hapus karakter khusus, keep only letters and spaces
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        # Hapus multiple spaces
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def detect_plagiarism(self, new_doc, ref_docs, threshold=0.7):
        """
        Deteksi plagiarisme
        
        Args:
            new_doc: Dictionary dengan 'name' dan 'content'
            ref_docs: List of dictionaries dengan 'name' dan 'content'
            threshold: Threshold similarity
            
        Returns:
            Dictionary berisi hasil deteksi
        """
        # Preprocess semua dokumen
        new_doc_content = self.preprocess_text(new_doc['content'])
        ref_contents = [self.preprocess_text(doc['content']) for doc in ref_docs]
        
        # Gabungkan semua dokumen untuk TF-IDF
        all_docs = [new_doc_content] + ref_contents
        
        # Hitung TF-IDF
        tfidf_matrix = self.vectorizer.fit_transform(all_docs)
        
        # Hitung Cosine Similarity
        # Bandingkan dokumen baru (index 0) dengan semua referensi (index 1+)
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        
        # Buat hasil
        results = []
        for idx, sim in enumerate(similarities):
            results.append({
                'doc_name': ref_docs[idx]['name'],
                'similarity': float(sim),
                'is_plagiarized': sim > threshold,
                'matched_phrases': self.find_similar_phrases(
                    new_doc['content'], 
                    ref_docs[idx]['content']
                ) if sim > threshold else []
            })
        
        # Sort by similarity (descending)
        results.sort(key=lambda x: x['similarity'], reverse=True)
        
        # Statistik
        plagiarized = [r for r in results if r['is_plagiarized']]
        stats = {
            'total_checked': len(results),
            'plagiarized_count': len(plagiarized),
            'max_similarity': max(similarities),
            'avg_similarity': np.mean(similarities),
            'min_similarity': min(similarities)
        }
        
        return {
            'results': results,
            'plagiarized': plagiarized,
            'stats': stats,
            'tfidf_matrix': tfidf_matrix,
            'similarity_matrix': similarities
        }
    
    def find_similar_phrases(self, text1, text2, min_words=5, max_phrases=3):
        """
        Cari frasa yang mirip antara dua teks
        """
        words1 = text1.lower().split()
        words2 = text2.lower().split()
        
        matches = []
        
        # Cari frasa yang sama
        for i in range(len(words1) - min_words + 1):
            for length in range(min_words, min(16, len(words1) - i + 1)):
                phrase = ' '.join(words1[i:i+length])
                if phrase in text2.lower():
                    matches.append({
                        'phrase': phrase,
                        'length': length
                    })
        
        # Sort by length dan ambil top matches
        matches.sort(key=lambda x: x['length'], reverse=True)
        return matches[:max_phrases]
    
    def calculate_optimal_threshold(self, similarities, labels):
        """
        Hitung threshold optimal berdasarkan data
        Menggunakan metode F1-Score maksimal
        
        Args:
            similarities: Array of similarity scores
            labels: Array of true labels (1 = plagiat, 0 = bukan)
            
        Returns:
            Optimal threshold
        """
        thresholds = np.arange(0.1, 1.0, 0.05)
        best_threshold = 0.7
        best_f1 = 0
        
        for threshold in thresholds:
            predictions = (similarities > threshold).astype(int)
            
            # Hitung precision, recall, f1
            tp = np.sum((predictions == 1) & (labels == 1))
            fp = np.sum((predictions == 1) & (labels == 0))
            fn = np.sum((predictions == 0) & (labels == 1))
            
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            if f1 > best_f1:
                best_f1 = f1
                best_threshold = threshold
        
        return best_threshold, best_f1
    
    def highlight_text(self, text, phrases):
        highlighted = text
        for p in phrases:
            phrase = p['phrase']
            highlighted = highlighted.replace(
                phrase,
                f"**🟥 {phrase.upper()} 🟥**"
            )
        return highlighted
