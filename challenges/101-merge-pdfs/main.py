# Desafio 101: Unir dos pdfs en uno

# pip install pypdf

from pypdf import PdfWriter
import os

def merge_two_pdfs(pdf1_path, pdf2_path, output_path):
    try:
        merger = PdfWriter()
        
        merger.append(pdf1_path)
        merger.append(pdf2_path)
        
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))
        
        with open(output_path, "wb") as output_file:
            merger.write(output_file)
            
        merger.close()
        
        print(f"Successfully merged '{pdf1_path}' and '{pdf2_path}' into '{output_path}'.")
    
    except FileNotFoundError as e:
        print(f"Error: A PDF file was not found. Please check your paths. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
