import cv2

# 이미지 흑백 처리

# 1) 흑백으로 읽어오기 / cv2.IMREAD_GRAYSCALE
img = cv2.imread('dogs.jpg', cv2.IMREAD_GRAYSCALE)

# 2) BGR 이미지에서 GRAY로 변경 / cv2.cvtColor -> BT.601 공식 적용
img2 = cv2.imread('dogs.jpg')
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 3) Y = 0.299 * R + 0.587 * G + 0.114 * B    -> 흑백 공식을 이용하여 변경
img3 = cv2.imread('dogs.jpg')

img3_gray = (0.299 * img3[:, :, 2]) + (0.587 * img3[:, :, 1]) + (0.114 * img3[:, :, 0])

cv2.imwrite('dogs_img3_gray.jpg', img3_gray)
img3 = cv2.imread('dogs_img3_gray.jpg')

# 결과보기
cv2.imshow("img", img)
cv2.imshow("img2", img2_gray)
cv2.imshow("img3", img3)


cv2.waitKey(0)
cv2.destroyWindow()

