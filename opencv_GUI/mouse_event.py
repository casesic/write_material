import cv2 as cv 
import numpy as np 
#鼠标回调事件
def draw_circle(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDBLCLK:#鼠标左键点两下
        cv.circle(img,(x,y),100,(255,0,0),-1)
img=np.zeros((512,512,3),np.uint8)
#创建一个窗口,窗口是鼠标点击
cv.namedWindow('imager')
cv.setMouseCallback('imager',draw_circle)
cv.imshow('image',img)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1)&0xFF
    if k==ord('q'):
        break
cv.destroyAllWindows()