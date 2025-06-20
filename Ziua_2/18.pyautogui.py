# pip install PyAutoGUI
import pyautogui
import time

width, height = pyautogui.size()
print("Ecranul are:", width, " si inaltimea:", height)

close_position = (1626, 638)


time.sleep(5)

pyautogui.moveTo(close_position[0], close_position[1])

pyautogui.hotkey("cmd", "shift", "3")#

time.sleep(3)
pyautogui.click()


