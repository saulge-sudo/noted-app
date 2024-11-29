import pytesseract as pyts
import cv2 as cv
import time, os
from PIL import Image

def import_image():
    for i in range(4):
        print(i+1)
        time.sleep(1) #wait for 4 seconds to adjust the camera
        
    cap = cv.VideoCapture(0)
    ret, frame = cap.read()

    cv.imwrite(r'images/unchanged.jpg',frame)
    cv.destroyAllWindows()
    cap.release()

import_image()

pyts.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = Image.open(r"images/unchanged.jpg")

img.save('images/unchanged_sharp.jpg', quality=95)
text = pyts.image_to_string(img)

print(text)