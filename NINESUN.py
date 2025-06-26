import pyautogui
import keyboard
import time

def fire():# 篝火
    pyautogui.hotkey("e")
    time.sleep(3)
    pyautogui.hotkey('z')
    time.sleep(3)
    pyautogui.hotkey('x')
    time.sleep(3)

def jump():# 走跳
    pyautogui.keyDown("a")
    time.sleep(0.7)
    pyautogui.keyUp("a")
    time.sleep(0.3)

    pyautogui.keyDown("l")
    time.sleep(0.5)
    pyautogui.press('w')
    pyautogui.keyUp("l")
    
    pyautogui.keyDown("w")
    time.sleep(1)
    pyautogui.keyUp("w")

def atk():# 左走攻擊
    pyautogui.keyDown("a")
    time.sleep(0.8)
    pyautogui.keyUp("a")
    time.sleep(0.5)

    pyautogui.press('c')
    time.sleep(0.5)

    pyautogui.keyDown("d")
    time.sleep(1.5)
    pyautogui.keyUp("d")
    time.sleep(0.5)

def money():
    fire()
    jump()
    pyautogui.keyDown("a")
    time.sleep(0.8)
    pyautogui.keyUp("a")
    time.sleep(0.5)

    pyautogui.press('c')
    time.sleep(0.5)

    pyautogui.keyDown("a")
    time.sleep(2)
    pyautogui.keyUp("a")
    time.sleep(0.5)

    pyautogui.keyDown("l")
    time.sleep(0.05)
    pyautogui.press('k')
    pyautogui.keyUp("l")
    time.sleep(2)

    pyautogui.keyDown("d")
    time.sleep(1)
    pyautogui.keyUp("d")


    pyautogui.keyDown("l")
    time.sleep(0.05)
    pyautogui.press('k')
    pyautogui.keyUp("l")

    pyautogui.keyDown("d")
    time.sleep(1.9)
    pyautogui.keyUp("d")

def main():
    fire()
    jump()
    atk()
    time.sleep(1)

# 開機
start_time = time.time()
start_money = 768
time.sleep(10)

loop = 1
while True:
    if keyboard.is_pressed('q'):
        print("END")
        break
   
    if loop % 10 != 0:
        main()
    else:
        money()
    
    end_time = time.time()
    true_time = end_time - start_time
    hhh = int(true_time//3600)
    min = int(true_time//60)
    sec = int(true_time%60)
    print("第{0:4}次，目前金額{1:6}，花費時間：{2:4}小時{3:2}分{4:2}秒".format(loop,start_money+32*loop,hhh,min,sec) )
    
    time.sleep(3)
    loop += 1

print("第{0:4}次，目前金額{1:6}，花費時間：{2:4}小時{3:2}分{4:2}秒".format(loop,start_money+32*loop,hhh,min,sec) )
print("END")

