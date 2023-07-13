import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
img=cv.imread('D:\Program Files\opencv\photo3.jpg')
#阈值处理cv.threshold(src, thresh, maxval, type[, dst])
#cv.THRESH_BINARY表示大于阈值时置 255，否则置 0。
ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
#cv.THRESH_BINARY_INV表示大于阈值时置 0，否则置 255。
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
#cv.THRESH_TRUNC表示大于阈值时置为阈值 thresh，否则不变（保持原色）
ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
#cv.THRESH_TOZERO表示大于阈值时不变（保持原色），否则置 0。
ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
#cv.THRESH_TOZERO_INV表示大于阈值时置 0，否则不变（保持原色）
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    #plt.xticks获取或设置当前x轴刻度位置和标签。
    plt.xticks([]),plt.yticks([])
plt.show()
