#!/usr/bin/python

'''
This should be the final program
It does the following jobs
1- get a frame from the live webcam
2- convert to grayscale
3- run the face detection algo
4- if found, extract the face
5- save it with the timestamp.jpg  as its name
6- go to step 1
'''

import cv2
import sys
from datetime import datetime as dt


cascPath = sys.argv[1]
#cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#if (faceCascade = None ):
  #  face
wcam = cv2.VideoCapture(0)

#continously reads the frame from the webcam
while (wcam.isOpened()):

    ret, frame = wcam.read()
    timestamp = str(dt.now())[:-7]              #for trimming the microseconds
    gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                                    #grayscale image is required for the image detection algo

    '''face detection api
    using the grayscale image as a source
    higher scalefactor can result in the face not being detected
        while the lower value can cause the decrease in speed but decrease in precision
        '''
    faces = faceCascade.detectMultiScale(
        gframe,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize =(30, 30),
       # flags=cv2.CASCADE_SCALE_IMAGE
        )
    
    #extract the detected face and save it with the current timestamp
    for (x,y,w,h) in faces:
        face_frame = frame[y:y+h, x:x+w]
        cv2.imwrite(timestamp + ".jpg", face_frame)
      
        
    
wcam.release()
cv2.destroyAllWindows()


