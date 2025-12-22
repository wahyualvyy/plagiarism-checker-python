import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """
    Ekstrak teks dari file PDF
    
    Args:
        pdf_path: Path ke file PDF
        
    Returns:
        String berisi teks dari PDF
    """
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Ekstrak teks dari setiap halaman
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        
        return text
    except Exception as e:
        print(f"Error extracting PDF {pdf_path}: {str(e)}")
        return ""

def extract_text_from_txt(txt_path):
    """
    Baca teks dari file .txt
    
    Args:
        txt_path: Path ke file .txt
        
    Returns:
        String berisi teks dari file
    """
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error reading TXT {txt_path}: {str(e)}")
        return ""

def read_document(file_path):
    """
    Baca dokumen (PDF atau TXT)
    
    Args:
        file_path: Path ke file
        
    Returns:
        String berisi teks dari dokumen
    """
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Format file tidak didukung. Gunakan .pdf atau .txt")