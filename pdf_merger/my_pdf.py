import PyPDF2
import os

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Otwórz oba pliki PDF
    with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
        # Utwórz obiekty reader dla obu plików PDF
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        pdf2_reader = PyPDF2.PdfReader(pdf2_file)
        
        # Utwórz obiekt writer
        pdf_writer = PyPDF2.PdfWriter()
        
        # Dodaj strony z pierwszego pliku PDF
        for page_num in range(len(pdf1_reader.pages)):
            page = pdf1_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        # Dodaj strony z drugiego pliku PDF
        for page_num in range(len(pdf2_reader.pages)):
            page = pdf2_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        # Zapisz połączone pliki PDF do nowego pliku
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Przykładowe użycie funkcji merge_pdfs
if __name__ == "__main__":
    pdf1_path = 'plik1.pdf'
    pdf2_path = 'plik2.pdf'
    output_path = 'połączony_plik.pdf'
    merge_pdfs(pdf1_path, pdf2_path, output_path)
    print("Pliki PDF zostały połączone!")

def sprawdz_plik_pdf(sciezka):
    if os.path.exists(sciezka):  # sprawdza, czy ścieżka istnieje
        if os.path.isfile(sciezka):  # sprawdza, czy ścieżka prowadzi do pliku
            if sciezka.lower().endswith('.pdf'):  # sprawdza, czy plik kończy się na .pdf
                return True
    return False

