import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
#tạo một mặt nạ
mask = np.zeros(img.shape[:2],np.uint8)
#chỉ định mô hình nền
bgdModel = np.zeros((1,65),np.float64)
#chỉ định mô hình tiền cảnh
fgdModel = np.zeros((1,65),np.float64)
#start_x, start_y, width, height
rect = (161,79,150,150)
mask, bgdModel, fgdModel =cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()