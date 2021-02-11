import cv2

# 흑백으로 가져오기
img = cv2.imread('dogs.jpg',0)

# 가장자리 가져오기
# Canny(이미지, 최소 threshold, 최대 threshold, edges : 저장 변수, apertureSize : 그레디언트값 기본 3, L2gradient = 기본값 False) -> edges
img_canny = cv2.Canny(img, 50, 100)

cv2.imshow("img_canny", img_canny)
cv2.waitKey()
cv2.destroyWindow()