# Juan Trinidad
# CST 205
# Due 5/14/2018
# Description: Python file that takes a image and returns it back.
# When it does return it back, it displays the image with a box of where the nose is located at.
#The program also returns an array of where the nose is detected.

import cv2
import sys
from pprint import pprint
from PIL import Image

def nosedetect(path):
    nose_cascade = cv2.CascadeClassifier('nose.xml')

    if nose_cascade.empty():
        print('WARNING: Cascade did not load')

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    nose = nose_cascade.detectMultiScale(gray, 1.3, 5)
    pprint(nose)

    for (x,y,w,h) in nose:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(img, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 2)

    cv2.imwrite('newimagesss.png', img)
    im = Image.open('newimagesss.png')
    im.show()
