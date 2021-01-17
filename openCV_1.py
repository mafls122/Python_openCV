import cv2 as cv

img = cv.imread('dogs.jpg') # 파일 읽어오기

print(type(img))  # <class 'numpy.ndarray'>
print(img.dtype)  # uint8
print(img.shape)  # 행(높이), 열(폭), 색상(채널)  (655, 660, 3)

cv.imshow("Display window", img)

cv.waitKey(0)
cv.destroyWindow()

# 색상의 순서 BGR
# ex) im[:, :, (0,1)] = 0  -> 0번째 (B:파랑)과 1번째 (G;녹색) 을 0(검정)으로 지정
img[:, :, (0,1)] = 0

# cv.imwrite(파일이름, 대상)  파일 저장
cv.imwrite('dogs_red.jpg', img)

