import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('letters.jpg', cv2.IMREAD_GRAYSCALE)

# 5x5 크기의 1로 채워진 매트릭스 생성
kernel = np.ones((5, 5), np.uint8)

# 수축 : erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
erosion = cv2.erode(img, kernel, iterations=1)

# 팽창 : dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
dilates = cv2.dilate(img, kernel, iterations=1)

'''
# cv2.morphologyEx(src, op, kernel[, dst[, iterations[, borderType[, borderValue ]]]]) -> dst

# cv2.MORPH_CLOSE : 팽창 후 수축 ( closing )
# cv2.MORPH_OPEN : 수축 후 팽창 ( opening )
# cv2.MORPH_BLACKHAT : MORPH_CLOSE한 이미지와 원본 이미지의 차이를 표시
# cv2.MORPH_GRADIENT : 외곽선(테두리), dilation 이미지와 erosion 이미지의 차이
# cv2.MORPH_TOPHAT : 9*9의 커널 크기, 원본 이미지와 MORPH_OPEN한 이미지의 차이
'''
ret, img_th = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
img_res = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, kernel)

plt.subplot(141),plt.imshow(img),plt.title('original')
plt.subplot(142),plt.imshow(erosion),plt.title('erosion')
plt.subplot(143),plt.imshow(dilates),plt.title('dilate')
plt.subplot(144),plt.imshow(img_res),plt.title('img_res')

plt.show()

'''
모폴리지는 형태학적 방법을 영상으로 처리하는 것이며 침식과 팽창 연산을 한다.
    - 침식 : 객체의 크기가 축소하는 것을 말하며 영상내에서 작은 크기의 잡음 제거
    - 팽창 : 객체의 크기가 확대되면서 빈공간을 채울 때 사용
    - 열림 연산 : 침식 연산 후에 팽창을 수행, 침식은 객체가 축소되며 배경의 잡음들을 제거하고, 
                  팽창 연산으로 축소되었던 객체들이 원래 크기로 돌아간다.
    - 닫힌 연산 : 팽창 연산 후에 침식 연산을 수행한다. 팽창 연산으로 객체가 확장되어 객체 내부의 빈 공간이 매워진 후
                  침식 연산으로 확장되었던 객체의 크기를 원래대로 축소된다.
'''