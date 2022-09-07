from PyPDF2 import PdfFileMerger
import os

merged = PdfFileMerger()

file_path = r'pdf_files/'

for root, dirs, file_names in os.walk(file_path):
    
    for file_name in file_names:
        merged.append(file_path + file_name)

merged.write("merged_files.pdf")
merged.close()
