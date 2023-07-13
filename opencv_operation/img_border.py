#为图像创建边框
import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
BLUE=[0,255,0]
img=cv.imread('D:/Program Files/opencv/tree.jpg')
#参数：src-输入图像，top bottom left right，borderType-边界类型的标志
replicate=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect101=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
wrap=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
constant=cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
#plt.subplot(221)表示将整个图像窗口分为2行2列, 当前位置为1.
#plt.imshow()参数：图像，颜色图谱（colormap), 默认绘制为RGB(A)颜色空间。
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
#展示图像
plt.show()
