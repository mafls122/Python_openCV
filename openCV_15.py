# 이미지를 히스토그램으로 시각화 : cv2.calcHist()
# -> 이미지에서 G, R, B를 가진 화소로 구성된 것을 그래프로 표현
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dogs.jpg')
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 255])

plt.show()