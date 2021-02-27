import cv2
import numpy as np

img01 = np.zeros((300, 300), np.uint8)
img02 = img01.copy()

h, w = img01.shape[:2]
cx, cy = w//2, h//2
cv2.circle(img01, (cx,cy), 100, 255, -1)  # 흰색 원 그리기
cv2.rectangle(img02, (0, 0, cx, h), 255, -1)  # 흰색 사각형 그리기

img_or = cv2.bitwise_or(img01, img02)  # 논리합
img_and = cv2.bitwise_and(img01, img02)  # 논리곱
img_xor = cv2.bitwise_xor(img01, img02)  # 배타논리합
img_not = cv2.bitwise_not(img01)  # 행렬 반전

cv2.imshow("img01", img01)
cv2.imshow("img02", img02)
cv2.imshow("img_or", img_or)
cv2.imshow("img_and", img_and)
cv2.imshow("img_xor", img_xor)
cv2.imshow("img_not", img_not)

cv2.waitKey(0)
cv2.destroyAllWindows()