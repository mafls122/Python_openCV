import cv2
import matplotlib.pyplot as plt

# 1. 이미지 흑백으로 읽어오기
image = cv2.imread('dogs.jpg', cv2.IMREAD_GRAYSCALE)

# 임계값 처리 : cv2.threshold( src, thresh, maxval, type[ , dst] )
th, im_th = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print(th)
plt.imshow(im_th)
cv2.imshow("img", im_th)

# 예1) cv2.THRESH_TOZERO : 임계값보다 큰 값은 원래의 상태로 작은 값은 0으로 지정
th2, im_th2 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
print(th2)
plt.imshow(im_th2)
cv2.imshow("img2", im_th2)

# 예2) cv2.THRESH_OTSU
th3, im_th3 = cv2.threshold(image, 127, 255, cv2.THRESH_OTSU)
print(th3)
plt.imshow(im_th3)
cv2.imshow("img3", im_th3)

cv2.waitKey()

'''
cv2.THRESH_BINARY  :  픽셀값 src(x,y) thresh 값보다 크면 value, 작으면 0
cv2.THRESH_BINARY_INV  :  픽셀값 src(x,y) thresh 값보다 크면 0, 작으면 value 
cv2.THRESH_TRUNC  :  픽셀값 src(x,y) thresh 값보다 크면 thresh, 작으면 픽셀값 src(x,y)
cv2.THRESH_TOZERO  :  픽셀값 src(x,y) thresh 값보다 크면 픽셀값 src(x,y), 작으면 0
cv2.THRESH_TOZERO_INV  :  픽셀값 src(x,y) thresh 값보다 크면 0, 작으면 픽셀값 src(x,y)
'''