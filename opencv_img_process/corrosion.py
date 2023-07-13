#腐蚀
import cv2 as cv 
import numpy as np 
img=cv.imread('D:\Program Files\opencv\photo3.jpg')
kernel=np.ones((5,5),np.uint8)
erosion=cv.erode(img,kernel,iterations=1)#iterations，迭代的次数，默认值是1
cv.imshow('ero',erosion)
cv.waitKey(0)