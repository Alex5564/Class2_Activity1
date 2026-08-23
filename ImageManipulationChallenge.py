import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("original_images/spark.png")

if image is None:
    print("Error: Could not load image.")
else:
    # 2. Convert the Image to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(5, 5))
    plt.imshow(gray_image, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()

    cropped_image = image[100:300, 200:400]

    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(5, 5))
    plt.imshow(cropped_rgb)
    plt.title("Cropped Image")
    plt.axis("off")
    plt.show()

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

   
    brightened_image = cv2.add(image, np.array([50.0]))

    cv2.imwrite("output_images/grayscale.jpg", gray_image)
    cv2.imwrite("output_images/cropped.jpg", cropped_image)
    cv2.imwrite("output_images/rotated.jpg", rotated_image)
    cv2.imwrite("output_images/brightened.jpg", brightened_image)

    print("All processed images successfully saved to 'output_images'!")
