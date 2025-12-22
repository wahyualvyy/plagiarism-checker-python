import os
from pdf_extractor import read_document

def load_reference_documents(folder_path):
    """
    Load semua dokumen referensi dari folder
    
    Args:
        folder_path: Path folder berisi dokumen referensi
        
    Returns:
        List of dict {name, content}
    """
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf') or filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            content = read_document(file_path)

            if content.strip():
                documents.append({
                    'name': filename,
                    'content': content
                })

    return documents
