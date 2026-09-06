import pyautogui

gesture = input("Enter gesture: ")

if gesture == "up":
    pyautogui.scroll(500)
    print("Scrolling up")

elif gesture == "down":
    pyautogui.scroll(-500)
    print("Scrolling down")
