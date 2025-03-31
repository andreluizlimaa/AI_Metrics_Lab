from docling.document_converter import DocumentConverter
import torch

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

source = "/home/ian/Documents/códigos/DataViewer/AI_Metrics_Lab/pdf-ocr/ManualdeInterposicaodeRecursosAdvogadoProcurador.pdf"
converter = DocumentConverter()
print("Converting...")

result = converter.convert(source)
print("Conversion done!")
print("Exporting to markdown...")
print(result.document.export_to_markdown())  
print("Exported")