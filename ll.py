import pyautogui
import time

print("Keeping Teams status active...")

while True:
    # Move mouse slightly
    pyautogui.moveRel(1, 0, duration=0.1)
    pyautogui.moveRel(-1, 0, duration=0.1)

    # Wait 60 seconds
    time.sleep(60)