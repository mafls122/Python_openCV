import cv2

img = cv2.imread('dogs.jpg', 1)  # flag -> -1 : 변화없음, 0 : 그레이, 1 : 색상, 2 : 임의의 깊이, 3 : 임의의 색상

h = img.shape[0]
w = img.shape[1]
channel = img.shape[2]  # 컬러, 흑백 여러장 : 3D
print(h, w, channel)
# print(img.shape)

cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('img', 300, 300)  # 화면에 띄워지는 위치 지정

cv2.imshow('img', img)

cv2.waitKey(0)  # 0 입력 전까지 무한대기, 0 입력시 종료