import cv2
import numpy as np

cap = cv2.VideoCapture(0)

box_x = 300
box_y = 200
box_size = 60
box_color = (0, 255, 0)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(largest_contour) > 500:
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                object_x = int(M["m10"] / M["m00"])
                object_y = int(M["m01"] / M["m00"])
                
                cv2.circle(frame, (object_x, object_y), 5, (255, 255, 255), -1)

                if object_x < box_x: box_x -= 7
                if object_x > box_x: box_x += 7
                if object_y < box_y: box_y -= 7
                if object_y > box_y: box_y += 7
                
                if object_x < (width // 2):
                    box_color = (255, 0, 0)
                else:
                    box_color = (0, 0, 255)
                    
                if object_y < (height // 2):
                    box_size = 40
                else:
                    box_size = 100
    else:
        cv2.putText(frame, "Object missing!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        box_color = (0, 255, 0)

    cv2.rectangle(frame, (box_x, box_y), (box_x + box_size, box_y + box_size), box_color, -1)
    cv2.imshow("Gesture Control", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
