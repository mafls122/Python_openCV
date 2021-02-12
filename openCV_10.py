import cv2
import matplotlib.pyplot as plt

img = cv2.imread('dogs.jpg',cv2.COLOR_BGR2RGB)
# 이미지 블러 처리

# 1. blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst
blur = cv2.blur(img, (5, 5))

# 2. cv2.medianBlur(src, ksize[, dst])
mblur = cv2.medianBlur(img, 5)

# 3. cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst
# 비선형 필터를 구현할 때 사용, 밝기 변화가 심한 부분은 남겨두고 휘도 변화만 원만하게 만들어 준다.
bblur = cv2.bilateralFilter(img, 20, 250, 100)

# 4. cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
gblur = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(151), plt.imshow(img), plt.title('Original')
plt.subplot(152), plt.imshow(blur), plt.title('cv2.blur')
plt.subplot(153), plt.imshow(mblur), plt.title('cv2.medianblur')
plt.subplot(154), plt.imshow(bblur), plt.title('cv2.bilateralfiter_blur')
plt.subplot(155), plt.imshow(gblur), plt.title('cv2.Gaussianblur')

plt.show()