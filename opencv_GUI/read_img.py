import cv2 as cv 
import numpy as np 
import sys
img=cv.imread("tree.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window",img)
k=cv.waitKey(0)#0意味着永远等待，返回值是按下的键，唯一的参数是应该等待的时间
if k==ord("s"):#如果按下的是s,图像被写入一个文件
    cv.imwrite("tree.png",img)

