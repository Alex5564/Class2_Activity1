import cv2

image = cv2.imread('spark.png')
cv2.imshow("spark", image)

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()



