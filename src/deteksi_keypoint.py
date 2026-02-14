import cv2
import matplotlib.pyplot as plt

img = cv2.imread('posko1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()

kp, des = sift.detectAndCompute(gray, None)
img_with_kp = cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(img_with_kp, cv2.COLOR_BGR2RGB))  
plt.axis('off')
plt.show()