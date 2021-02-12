import cv2
import numpy as np

# 1) 이미지 가져오기
img = cv2.imread('dogs.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # BGR2HSV : H(색상), S(채도), V(명도) 로 변환

# 2) 추출 범위 지정 : cv2.inRange(대상, 시작 범위, 마지막 범위)
start_color = np.array([0, 50, 50])
end_color = np.array([255, 255, 255])
img_mask = cv2.inRange(hsv, start_color, end_color)

# 3) 원본 이미지와 mask 이미지 비교 : cv2.bitwise_and(대상, 대상, mask)
img_color = cv2.bitwise_and(img, img, mask = img_mask)

cv2.imshow("img", img)
cv2.imshow("img_mask", img_mask)
cv2.imshow("img_color", img_color)

cv2.waitKey()