import cv2
import numpy as np 

image = cv2.imread('spark.png')

img = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.line(img, (50, 50), (250, 50), (255, 255, 255), 2)

cv2.rectangle(img, (50, 100), (200, 200), (0, 255, 0), 2)

cv2.circle(img, (150, 150), 50, (255, 0, 0), 2)

height, width, channels = img.shape
print("width=", width)
print("height=", height)
print("channels=", channels)

cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWIndows()