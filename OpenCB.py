import cv2

image = cv2.imread('spark.png')
cv2.imshow("spark", image)

cv2.waitKey(0)
cv2.destroyAllWindows()



