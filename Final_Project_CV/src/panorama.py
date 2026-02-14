import cv2
import numpy as np
import matplotlib.pyplot as plt

img_kiri = cv2.imread('posko1.jpg')
img_kanan = cv2.imread('posko2.jpg')

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img_kiri, None)
kp2, des2 = sift.detectAndCompute(img_kanan, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

if len(good) > 10:
    src_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    h1, w1 = img_kiri.shape[:2]
    h2, w2 = img_kanan.shape[:2]
    
    hasil = cv2.warpPerspective(img_kanan, H, (w1 + w2, h1))
    
    hasil[0:h1, 0:w1] = img_kiri

    plt.figure(figsize=(20, 10))
    plt.imshow(cv2.cvtColor(hasil, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()