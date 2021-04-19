import pyautogui
import time
import subprocess
import os
pyautogui.PAUSE=1
os.system('taskkill /f /t /im AdmOrder1.exe')
subprocess.Popen('C:\Tch\exe\loginscreen.exe')
time.sleep(1)
#輸入帳號
pyautogui.moveTo(801,411,duration=0.2)
pyautogui.click()
pyautogui.typewrite('04053',interval=0.1)
#輸入密碼
pyautogui.press('tab')
pyautogui.typewrite('A44125',interval=0.1)
pyautogui.press('Alt'+'F4')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
#住院系統
pyautogui.moveTo(773,477,duration=0.2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.moveTo(300,300,duration=0.2)
pyautogui.click()
#離開提醒
time.sleep(5)
os.system('taskkill /f /t /im MRNotFinish.exe')
pyautogui.click()
