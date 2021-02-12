import cv2

# 이미지 흑백으로 읽어오기
image = cv2.imread('dogs.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 임계값 처리 : cv2.threshold( src, thresh, maxval, type[ , dst] ) : 임계값을 기준으로 흑/백으로 구분하는 함수
th, im_th = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print(th)
cv2.imshow("img", im_th)

# 예1) cv2.THRESH_TOZERO : 임계값보다 큰 값은 원래의 상태로 작은 값은 0으로 지정
th2, im_th2 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
print(th2)
cv2.imshow("img2", im_th2)

# 예2) cv2.THRESH_OTSU
th3, im_th3 = cv2.threshold(image, 127, 255, cv2.THRESH_OTSU)
print(th3)
cv2.imshow("img3", im_th3)

# 2. 적응 임계점 처리 : cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
# -> 주변 픽셀의 강도에 의해 임계값을 자동으로 결정함, 전체 픽셀을 기준으로 임계 값을 적용하지 않음

# ADAPTIVE_THRESH_MEAN_C : 픽셀 값의 평균에서 C를 뺀 값을 임계점으로 설정
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)
cv2.imshow('thres2' ,cv2.cvtColor(thres2, cv2.COLOR_GRAY2RGB))

# ADAPTIVE_THRESH_GAUSSIAN_C : Gaussian 윈도우 기반의 가중치들의 합에서 C를 뺀 값을 임계점으로 설정
# 중간이 가중치가 높고 멀어질 수록 가중치가 낮아짐
thres3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)
cv2.imshow('thres3' ,cv2.cvtColor(thres3, cv2.COLOR_GRAY2RGB))

cv2.waitKey()

'''
thresh : 임계값
cv2.THRESH_BINARY  :  픽셀값 src(x,y) thresh 값보다 크면 value, 작으면 0
cv2.THRESH_BINARY_INV  :  픽셀값 src(x,y) thresh 값보다 크면 0, 작으면 value 
cv2.THRESH_TRUNC  :  픽셀값 src(x,y) thresh 값보다 크면 임계값(thresh), 작으면 픽셀값 src(x,y)
cv2.THRESH_TOZERO  :  픽셀값 src(x,y) thresh 값보다 크면 픽셀값 src(x,y), 작으면 0
cv2.THRESH_TOZERO_INV  :  픽셀값 src(x,y) thresh 값보다 크면 0, 작으면 픽셀값 src(x,y)
'''