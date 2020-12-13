import pyautogui, time
time.sleep(4)
t=open("text", 'r')
for word in t:
    pyautogui.typewrite(word)
pyautogui.press("enter")     

