import pyautogui
import time
print('Press Ctrl-c to quit')


try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: {} ; Y: {}\n'.format(str(x).rjust(4),str(y).rjust(4))
        print(positionStr, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('\nDone.')

print('\b'*len(positionStr), end='', flush=True)

