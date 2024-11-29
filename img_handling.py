import pytesseract as pyts
import cv2 as cv
import time, os
from PIL import Image

def import_image():
    cap = cv.VideoCapture(0)
    ret, frame = cap.read()
    time.sleep(2) #wait for 2 seconds to adjust the camera
        
    cv.imwrite(r'images\unchanged.jpg',frame)
    cv.destroyAllWindows()
    cap.release()

import_image()

pyts.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open(r"images\unchanged.jpg")
text = pyts.image_to_string(img)

print(text)