import cv2 as cv 
import numpy as np
img=cv.imread('D:\Program Files\opencv\photo3.jpg') 
#cv.useOptimized()检查优化是否启动
a=cv.useOptimized()
print(a)
res=cv.medianBlur(img,49)
#用cv.setUseOptimized()来启用和禁用优化
cv.setUseOptimized(False)
b=cv.useOptimized()
print(b)
#衡量性能
x=5
#%timeit y=x**2(ipython中)
