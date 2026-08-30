import cv2
import numpy as np

def apply_tint(image, color):
  
    tinted = np.zeros_like(image)
    if color == 'r':
        tinted[:, :, 2] = image[:, :, 2]  
    elif color == 'g':
        tinted[:, :, 1] = image[:, :, 1]  
    elif color == 'b':
        tinted[:, :, 0] = image[:, :, 0] 
    return tinted

def apply_sobel(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    
    sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    return sobel_combined

def apply_canny(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_edges = cv2.Canny(gray, 100, 200)
    return canny_edges

def main():
    image_path = 'image.jpg'
    original_img = cv2.imread(image_path)
    
    if original_img is None:
        print(f"Error: Could not load image.")
        return

    current_display = original_img.copy()
    window_name = "Real-Time Filters and Edge Detection"
    cv2.namedWindow(window_name)
    
    print("--- Controls ---")
    print("'r' : Red Tint  | 'g' : Green Tint | 'b' : Blue Tint")
    print("'s' : Sobel     | 'c' : Canny Edge ")
    print("'o' : Reset Original Image")
    print("'q' : End Program\n")

    while True:
        cv2.imshow(window_name, current_display)
        
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('q'):
            print("Ending program...")
            break
            
        elif key == ord('r'):
            print("Applied Red Tint")
            current_display = apply_tint(original_img, 'r')
            
        elif key == ord('g'):
            print("Applied Green Tint")
            current_display = apply_tint(original_img, 'g')
            
        elif key == ord('b'):
            print("Applied Blue Tint")
            current_display = apply_tint(original_img, 'b')
            
        elif key == ord('s'):
            print("Applied Sobel Edge Detection")
            current_display = apply_sobel(original_img)
            
        elif key == ord('c'):
            print("Applied Canny Edge Detection")
            current_display = apply_canny(original_img)
            
        elif key == ord('o'):
            print("Reset to Original Image")
            current_display = original_img.copy()
            
        else:
            print(f"Invalid input: Please try again.")


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
