from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open("test.png")
image.show()
result = pytesseract.image_to_string(image, lang="eng")
print(result)