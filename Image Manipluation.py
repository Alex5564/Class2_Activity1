import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("original_images/spark.png") 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image.")
plt.axis('off') 
plt.show()

cropped_img = img[100:300, 200:400]

(h, w) = img.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

brightness_matrix = np.ones(img.shape, dtype="uint8") * 50
brightened_img = cv2.add(img, brightness_matrix)

cv2.imwrite("output_images/grayscale.jpg", gray_img)
cv2.imwrite("output_images/cropped.jpg", cropped_img)
cv2.imwrite("output_images/rotated.jpg", rotated_img)
cv2.imwrite("output_images/brightened.jpg", brightened_img)
