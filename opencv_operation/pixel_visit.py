import cv2 as cv 
import numpy as np
#加载彩色图像
img=cv.imread('tree.jpg')
#通过行列坐标访问像素值
px=img[100,100]
print(px)
blue=img[100,100,0]
print(blue)
#通过行列坐标修改像素值
img[100,100]=[255,255.255]
print(img[100,100])
#更好的像素访问和修改,选择数组的某个区域
img.item(10,10,2)#访问
img.itemset((10,10,2),100)
#访问图像的属性：行，列，通道的数量
print(img.shape)#(342,538,3)
#总像素数
print(img.size)
#图像数据类型
print(img.dtype)
#ROI复制
ball=img[280:340,330:390]
img[273:333,100:160]=ball
#分割bgr通道
b,g,r=cv.split(img)
b=img[:,:,0]
#合并bgr通道
img=cv.merge((b,g,r))
#把所有的红色像素设置为0
img[:,:,2]=0


 