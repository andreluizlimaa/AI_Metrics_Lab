import os
from pdf2image import convert_from_path

def pdf_to_image(pdf_path, image_folder_path):
    # Criar a pasta se ela não existir
    os.makedirs(image_folder_path, exist_ok=True)
    
    # Converter PDF para imagens
    pages = convert_from_path(pdf_path, dpi=1000, output_folder=image_folder_path)

    for count, page in enumerate(pages):
        page.save(f'out{count}.jpg', 'JPEG')