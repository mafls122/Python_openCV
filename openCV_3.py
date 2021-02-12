import cv2

# 이미지 연결
img1 = cv2.imread("dogs.jpg")
img2 = cv2.imread("lovedogs.jpg")

# 1) 같은 이미지 세로로 붙이기
img_v = cv2.vconcat([img1, img1])
cv2.imshow("img_vconcat", img_v)

# 2) 같은 이미지 가로로 붙이기
img_h = cv2.hconcat([img1, img1])
cv2.imshow("img_hconcat", img_h)

# 3) 크기가 다른 이미지 세로로 붙이기 함수 구현
def vconcat_img(img_list, interpolation = cv2.INTER_CUBIC):

    w_min = min(img.shape[1] for img in img_list)  # 이미지 중 가로가 작은 값을 리턴
    # 가로의 사이즈 재조정
    img_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation) for im in img_list]

    return cv2.vconcat(img_list_resize)  # 결합해서 리턴

img_v_resize = vconcat_img ([img1, img2])
cv2.imshow("img_vconcat_resize", img_v_resize)

# 4) 바둑판 타일형 만들기
def img_tile(img_list):
    return cv2.vconcat([cv2.hconcat(img) for img in img_list])

img_tile_res = img_tile( [[ img1, img1, img1 ], [ img1, img1, img1 ], [ img1, img1, img1 ]] )
cv2.imshow("img_tile", img_tile_res)

cv2.waitKey(0)
cv2.destroyWindow()