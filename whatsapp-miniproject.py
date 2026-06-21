import pyautogui as py

import time

time.sleep(3)

py.press("win")
time.sleep(2)
py.write("whatsapp")
time.sleep(1)
py.press("enter")
time.sleep(3)
py.hotkey("ctrl","f")
time.sleep(2)
py.write("+977 9818954396")
time.sleep(2)
py.press("enter")
time.sleep(3)
assignment="Hello devansh I am samriddha :>"
py.write(assignment)
time.sleep(2)
py.press("enter")
print("WhatsApp Automation Completed Sucessfully")