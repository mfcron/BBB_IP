#!/usr/bin/env python
#-*- coding:utf-8 -*-

#works fine with python v2 and v2.7
#but not with v3 +
 
import cv2
import sys

#from cv2 import *

# Get user supplied values
imagePath = sys.argv[1]#"abba.png"
cascPath = sys.argv[2]#"haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!").format(len(faces))

i=0#
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #sub_face[i] = image[y:y+h, x:x+w]#
    cv2.imwrite(str(i)+".jpg", image[y:y+h, x:x+w])#
    ++i
	
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)

