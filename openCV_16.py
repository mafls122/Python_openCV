# 이미지 변환 : 감마 처리 (밝기)
# y = 255*(x/255) ^ (1/r) : r의 값이 1보다 크면 밝고 1보다 작으면 어둡다.
# LUT (src, lut[, dst]) -> dst
import cv2
import numpy as np

r = 1.8
lookup_table = np.zeros((256, 1), dtype = 'uint8')
print(lookup_table)

for i in range(256):
    lookup_table[i][0] = 255 * pow(float(i)/255, 1.0/r)   # 공식

img = cv2.imread('dogs.jpg', 1)  # 이미지 로드
img_gamma = cv2.LUT(img, lookup_table)  # 감마 처리

cv2.imshow('img', img_gamma)
cv2.waitKey(0)



