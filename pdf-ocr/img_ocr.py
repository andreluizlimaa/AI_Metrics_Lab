from PIL import Image
import pytesseract
import numpy as np

filename = '/home/ian/Documents/códigos/DataViewer/AI_Metrics_Lab/pdf-ocr/out41.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)