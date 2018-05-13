# Juan Trinidad
# CST 205
# Due 5/14/2018
# Description: Python file that takes a image and returns it back.
# When it does return it back, it displays the image with a box of where the eyes is located at.
#The program also returns an array of where the eyes is detected.

import numpy as np
import cv2
from pprint import pprint
from PIL import Image

def eyedetect(path):
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    if eye_cascade.empty():
        print('WARNING: Cascade did not load')

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eye = eye_cascade.detectMultiScale(gray, 1.3, 5)
    pprint(eye)

    for (x,y,w,h) in eye:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)


    cv2.imwrite('newimages.png', img)
    im = Image.open('newimages.png')
    im.show()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
