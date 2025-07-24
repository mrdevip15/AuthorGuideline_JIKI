#!/usr/bin/env python3
import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- PAGE {page_num + 1} ---\n"
                text += page.extract_text()
                text += "\n"
            return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

if __name__ == "__main__":
    pdf_file = "Draft_Revisi_Fauzan Husain.pdf"
    extracted_text = extract_text_from_pdf(pdf_file)
    print(extracted_text) 