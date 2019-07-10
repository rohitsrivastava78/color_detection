#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:02:07 2019

@author: rohit
"""

import cv2, time
import numpy as np


video_path = 'video/color_object1.avi'
cap = cv2.VideoCapture(video_path)

while(1):

    # Take each frame
    status, frame = cap.read()
    
    if ( cap.isOpened() == False or status == False ): 
        print("Unable to read camera feed in loop !!! ")
        time.sleep(1)
        break
    
    

    # Convert BGR to HSV    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    # define range of all dark color in HSV
    lower_color = np.array([0,50,150])
    upper_color = np.array([179,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break   

cv2.destroyAllWindows()