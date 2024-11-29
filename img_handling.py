import pytesseract as pyts
import cv2 as cv
import time, os
from PIL import Image

cap = cv.VideoCapture(0)
ret, frame = cap.read()
time.sleep(2) #wait for 2 seconds to adjust the camera

while(True):
    cv.imshow('img1',frame) #display the captured image
    if cv.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv.imwrite(r'images\c1.png',frame)
        cv.destroyAllWindows()
        break

print(pyts.image_to_string(r'images\c1.png'))

cap.release()