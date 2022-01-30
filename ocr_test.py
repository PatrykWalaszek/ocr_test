import cv2  # pip install opencv-python
import pytesseract # pip install pytesseract and tesseract pip install tesseract-ocr
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread('./IMG_2037.jpg')

print(pytesseract.image_to_string(img))