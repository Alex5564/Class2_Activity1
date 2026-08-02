import cv2


image = cv2.imread('spark.png', cv2.IMREAD_UNCHANGED)

if image is None:
    print("Error: Could not open or find the image.")
else:
    print(f"Loaded image shape: {image.shape}")

    resized_tasks = [
        {"size": (200, 200), "filename": "input_image_small.png", "label": "Small"},
        {"size": (400, 400), "filename": "input_image_medium.png", "label": "Medium"},
        {"size": (600, 600), "filename": "input_image_large.png", "label": "Large"}
    ]

    for task in resized_tasks:
        resized_image = cv2.resize(image, task["size"], interpolation=cv2.INTER_AREA)
        
    cv2.imshow(f"Resized - {task['label']}", resized_image)
        
    cv2.imwrite(task["filename"], resized_image)
    print(f"Saved transparent PNG: {task['filename']}")

    print("Press any key on an image window to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
