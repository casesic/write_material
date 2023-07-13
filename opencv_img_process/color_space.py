import cv2 as cv 
import numpy as np 
#BGR<->GRAY
img=cv.imread('D:\Program Files\opencv\W2.jpg')
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#BGR<->HSV
img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)

