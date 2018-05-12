# Thomas Lopes
# 05/12/2018
# This code takes a file named mustache.png and past it on every faces of an image named Faces.jpg

import numpy as np
from PIL import Image
import cv2
from pprint import pprint

def pastFilterCV(faces,settings,toPast):    #This function is pasting a resized mustache on the faces image
    wFaces, hFaces = faces.shape[:2]
    wPast,hPast = toPast.shape[:2]
    print("size faces : ", end = "")
    print(wFaces,hFaces)
    print("size past : ", end = "")
    print(wPast,hPast)

    for x in range(wPast):
        for y in range(hPast):
            if (toPast[x,y][3] > 20):
                faces[x + settings[1] + int(settings[3] * 0.6), y + settings[0] + int(settings[2] * 0.25)] = (toPast[x,y][0], toPast[x,y][1], toPast[x,y][2])
    cv2.imwrite('facesmustached.jpg', faces)

casc_class = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('# WARNING: Cascade did not load')

img = cv2.imread('Faces.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.1, 9)

#for(x,y,h,w) in faces:
#    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

must = cv2.imread('mustache.png', cv2.IMREAD_UNCHANGED)
for(x,y,w,h) in faces:
    newMustache = cv2.resize(must, (int(w * 0.5), int(h * 0.1)))

    toPast = newMustache
    Faces = img
    pastFilterCV(Faces,(x,y,w,h), toPast)


Image.open('facesmustached.jpg').show()
