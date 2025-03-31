import fitz
import os

images_folder = "images"
pdffile = "/home/ian/Documents/códigos/DataViewer/AI_Metrics_Lab/pdf-ocr/ManualdeInterposicaodeRecursosAdvogadoProcurador.pdf"

os.makedirs(images_folder, exist_ok=True)

doc = fitz.open(pdffile)
zoom = 4
mat = fitz.Matrix(zoom, zoom)
count = 0

for p in doc:
    count += 1
for i in range(count):
    val = f"image_{i+1}.png"
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"{images_folder}/{val}")
doc.close()

#reader = easyocr.Reader(['en'])
#result = reader.readtext("image_1.png", detail=0)