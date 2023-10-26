import cv2
from PIL import Image
from pytesseract import pytesseract

cap = cv2.VideoCapture(0)

while True:
    _,image = cap.read()
    cv2.imshow('preview',image)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite('test1.jpg',image)
        break
cap.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract=r"C:\Users\Lenovo\AppData\Local\tesseract.exe"
    image_path='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])
tesseract()
