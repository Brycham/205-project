# Juan Trinidad
# CST 205
# Due 5/14/2018
# Description: Python file that takes a image and returns it back.
# When it does return it back, it displays the image with a box of where the face is located at.
#The program also returns an array of where the face is detected.

import numpy as np
import cv2
from pprint import pprint

casc_class = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 9)

pprint(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imwrite('faceDetect.jpg', img)
