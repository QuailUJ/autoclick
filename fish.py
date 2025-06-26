import pyautogui
import random
import time
cnt = 0
time.sleep(2)

while True:
    try:    
        for i in range(100):
            pyautogui.dragTo(random.randint(100,1820),random.randint(100,980), duration=0.5, button='right')
            cnt += 1
        time.sleep(10)
    except:
        print(f"執行次數:{cnt}")