import easyocr

reader = easyocr.Reader(['pt'], gpu=False)
result = reader.readtext("images/image_2.png", detail=0)
print(result)
