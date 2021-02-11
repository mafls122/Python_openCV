import cv2
import matplotlib.pyplot as plt

# 파일 업로드
img = cv2.imread('dogs.jpg')
# 이미지 파일 픽셀 및 크기 확인
print(img.shape)
print(img.size)

# 100, 100의 픽셀을 px에 저장
px = img[100, 100]
# B G R 순서대로 출력 ( 흑백의 경우 구분안됨)
print(px)
# R 값만 출력
print(px[2])

# (100,100) 픽셀 값만 0 으로 변경
img[0:100, 0:100] = [ 0, 0, 0]

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# ROI 추출 및 복사
roi = img[400:550, 50:200] # 추출

img[0:150, 0:150] = roi # 복사

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# 픽셀별 색상 다루기
# Red 색상을 0으로 변경 ( B G R 순서 )
img[ :, :, 2 ] = 0
plt.imshow(img)
plt.show()
