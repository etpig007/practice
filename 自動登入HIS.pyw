import pyautogui
import time
import subprocess
import os
command = 'taskkill /f /t /im AdmOrder1.exe'
os.system(command)
subprocess.Popen('C://Tch/exe/loginscreen.exe')
time.sleep(0.5)
#輸入帳號
pyautogui.moveTo(801,411,duration=0.2)
pyautogui.click()
pyautogui.typewrite('04053',interval=0.1)
#輸入密碼
pyautogui.moveTo(797,439,duration=0.2)
pyautogui.click()
pyautogui.typewrite('A44125',interval=0.1)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
#按Enter
pyautogui.moveTo(1018,411,duration=0.2)
pyautogui.doubleClick()
time.sleep(0.5)
pyautogui.press('enter')
#住院系統
pyautogui.moveTo(773,477,duration=0.2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.moveTo(300,300,duration=0.2)
pyautogui.click()
#離開提醒
time.sleep(5)
pyautogui.moveTo(629,648,duration=0.2)
pyautogui.click()
