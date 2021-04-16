import pyautogui
import subprocess
import os
import time
pyautogui.PAUSE=0.5
command = 'taskkill /f /t /im AdmOrder1.exe'
os.system(command)
subprocess.Popen('C://Tch/exe/loginscreen.exe')

account='haha'
pasw='nono'
#輸入帳號
pyautogui.moveTo(801,411,duration=0.2)
pyautogui.click()
pyautogui.typewrite(account,interval=0.1)
#輸入密碼
pyautogui.moveTo(797,439,duration=0.2)
pyautogui.click()
pyautogui.typewrite(pasw,interval=0.1)
pyautogui.press('enter')
pyautogui.press('enter')
#按Enter
pyautogui.moveTo(1018,411,duration=0.2)
pyautogui.doubleClick()
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
