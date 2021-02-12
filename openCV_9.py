import cv2

img = cv2.imread('dogs.jpg', cv2.COLOR_BGR2RGB)

# 1. cv2.add() : Saturation 연산 수행-> 0보다 작으면 0, 255보다 크면 255로 표현
res = cv2.add(img, img)
cv2.imshow('img_add', res)

# 2. np.add() : Modulo 연산 수행 -> 256은 0, 257은 1로 표현 (256의 나머지를 통해 0,1로 구분)
res2 = img + img
cv2.imshow('img_np_add', res2)

cv2.waitKey()