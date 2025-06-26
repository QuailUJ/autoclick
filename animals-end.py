import pyautogui
import keyboard
import time

time.sleep(3)
cnt = 0

def eat():
    pyautogui.click(1850,1040)
    for _ in range(50):
        pyautogui.click(870,1040)
    pyautogui.rightClick()

def money():
    pyautogui.moveTo(0, 1070)
    pyautogui.moveTo(1080,1070, duration=2) 
    for i in range(200):
        pyautogui.tripleClick(100+i*8.5,1060)
        time.sleep(0.25)
    pyautogui.moveTo(0, 1070)
    pyautogui.moveTo(1920,1070, duration=2) 



while True:
    if keyboard.is_pressed('1'):
        print("END",end=" ")
        print(cnt)
        break
    money()
    eat()
    
    time.sleep(10)
    cnt += 1