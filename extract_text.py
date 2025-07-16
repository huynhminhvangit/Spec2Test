"""
Text Extraction Module

Handles extraction of text content from various document formats:
- PDF files
- DOCX files  
- TXT files
"""

import os
from pathlib import Path

try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

try:
    from docx import Document
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text content from a PDF file."""
    if not PDF_AVAILABLE:
        raise ImportError("PyPDF2 is required to read PDF files. Install with: pip install PyPDF2")
    
    text_content = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text_content += page.extract_text() + "\n"
    except Exception as e:
        raise Exception(f"Error reading PDF file: {e}")
    
    return text_content


def extract_text_from_docx(file_path: str) -> str:
    """Extract text content from a DOCX file."""
    if not DOCX_AVAILABLE:
        raise ImportError("python-docx is required to read DOCX files. Install with: pip install python-docx")
    
    text_content = ""
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            text_content += paragraph.text + "\n"
    except Exception as e:
        raise Exception(f"Error reading DOCX file: {e}")
    
    return text_content


def extract_text_from_txt(file_path: str) -> str:
    """Extract text content from a TXT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()
        except Exception as e:
            raise Exception(f"Error reading TXT file: {e}")
    except Exception as e:
        raise Exception(f"Error reading TXT file: {e}")


def extract_text_from_file(file_path: str) -> str:
    """
    Extract text from a file based on its extension.
    
    Supported formats: PDF, DOCX, TXT
    """
    path = Path(file_path)
    extension = path.suffix.lower()
    
    if extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif extension == '.docx':
        return extract_text_from_docx(file_path)
    elif extension == '.txt':
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}. Supported formats: .pdf, .docx, .txt")
