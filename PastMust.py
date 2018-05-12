import numpy as np
from PIL import Image
import cv2
from pprint import pprint

def pastFilter(faces, settings, toPast):
    print(toPast.mode)
    for x in range(toPast.width):
        for y in range(toPast.height):
            #if toPast.getpixel((x,y))[3] > 20:
                faces.putpixel((x + settings[0] + int(settings[2] * 0.25), y + settings[1] + int(settings[3] * 0.6)), toPast.getpixel((x,y)))
            # faces.putpixel((x + settings[0], y + settings[1]), toPast.getpixel((x,y)))
            #print("putpixel")

def pastFilterCV(faces,settings,toPast):
    wFaces, hFaces = faces.shape[:2]
    wPast,hPast = toPast.shape[:2]
    print("size faces : ", end = "")
    print(wFaces,hFaces)
    print("size past : ", end = "")
    print(wPast,hPast)

    for x in range(wPast):
        for y in range(hPast):
            #print(toPast[x,y])
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

#pprint(faces)

for(x,y,h,w) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


# cv2.imwrite('new.jpg', img)
must = cv2.imread('mustache.png', cv2.IMREAD_UNCHANGED)
for(x,y,w,h) in faces:
    newMustache = cv2.resize(must, (int(w * 0.5), int(h * 0.1)))
    # print("resize as : ", end = "")
    # print(w * 0.1, end = "")
    # print(", ", end = "")
    # print(h * 0.5)
    # cv2.imwrite('newMustache.png', newMustache)
    # toPast = Image.open('newMustache.png')
    # # toPast = Image.open('Logo.jpg')
    toPast = newMustache
    # Faces = Image.open('new.jpg')
    Faces = img
    # #print("image")
    # pastFilter(Faces, (x,y,w,h), toPast)
    pastFilterCV(Faces,(x,y,w,h), toPast)
    # Faces.save("new.jpg")
    #Faces.show()


Image.open('facesmustached.jpg').show()
