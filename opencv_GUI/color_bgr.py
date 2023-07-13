#轨迹条作为调色板
import numpy as np 
import cv2 as cv 
def nothing(x):
    pass
img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')
#三个轨迹条指定B,G,R的颜色
#参数:轨迹条的名称，所连接的窗口名称，默认值，最大值，回调函数
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv.imshow('image',img)
    #cv2.waitKey(1)：返回与按下键值对应的32位整数。
    k=cv.waitKey(1)&0xFF
    if k==27:
        break
    #返回指定trackbar的当前位置，参数：trackbar的名字,trackbar父窗口的名字
    r=cv.getTrackbarPos('R','image')
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv.destroyAllWindows()
    