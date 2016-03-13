import cv2
import numpy as np

cap = cv2.VideoCapture("vtest.mp4")

while(cap.isOpened()):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([10,0,200])
    upper_red = np.array([255,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    img = cv2.imread('games.jpg',0)
    edges = cv2.Canny(mask,100,200)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('edges',edges)

    k = cv2.waitKey(60) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
