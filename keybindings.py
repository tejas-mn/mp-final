import os
import subprocess
from tkinter import *
import pyautogui
import pydirectinput

pressed = False

def fun(serial_data, text):
    global pressed
    
    if 'B44B9B44' in serial_data:               #Vol+
        text.insert(END, 'volume up\n')
        print("Volume UP")
        pyautogui.press('volumeup', 10)
    elif 'B54A9B44' in serial_data:             #Vol-
        pyautogui.press('volumedown', 10)
    elif '20DF00FF' in serial_data:             #PG+
        pyautogui.press('pageup')
    elif '20DF807F' in serial_data:             #PG
        pyautogui.press('pagedown')             
    elif 'F9069B44' in serial_data:             #OK
        text.insert(END, 'enter\n')
        pyautogui.press('enter')
    elif 'EC139B44' in serial_data:             #back
        pyautogui.press('backspace')
    elif 'E41B9B44' in serial_data:             #1
        os.system('explorer')
    elif 'F40B9B44' in serial_data:             #power button
        pyautogui.hotkey('alt' , 'f4')
    elif 'E7189B44' in serial_data:             
        pydirectinput.press('up')
    elif 'E9169B44' in serial_data:
        pydirectinput.press('down')
    elif '9B649B44' in serial_data:
        pydirectinput.press('left')
    elif '9A659B44' in serial_data:
        pydirectinput.press('right')
    elif 'FA059B44' in serial_data:             #bottom red
        pyautogui.press('win')
    elif 'B34C9B44' in serial_data:            #ch-
        if pressed:
            pressed = False
        pyautogui.hotkey('ctrl' , 'left')
    elif 'B24D9B44' in serial_data:             #ch+
        if pressed:
            pressed = False
        pyautogui.hotkey('ctrl' , 'right')
    elif 'EF19B44' in serial_data:              #tv button area
        pyautogui.hotkey('win' , 'm')
    elif 'F00F9B44' in serial_data:             #2
        os.system('spotify.exe')
    elif 'AB549B44' in serial_data:             #play icon
        pyautogui.press('space')
    elif 'EF109B44' in serial_data:             #recall
        if not pressed:
            pyautogui.hotkey('alt' , 'tab')  # hold down the shift key
            pyautogui.keyDown('alt')
            pressed = True
        else:
            pyautogui.keyUp('alt')  
            pressed = False
    elif 'E11E9B44' in  serial_data:            #bottom blue ppt flscrn
        pyautogui.press('f5')
    elif 'E31C9B44' in serial_data:             
        pyautogui.press('esc') 
    elif 'EA159B44' in serial_data:             #PG+
        pyautogui.press('pageup')
    elif 'EB149B44' in serial_data:             #PG-
        pyautogui.press('pagedown')
    elif 'E6199B44' in serial_data:             #4
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif 'FC039B44' in serial_data:             #3
        pyautogui.hotkey('win' , '1');
    elif 'EE119B44' in serial_data:             #5
        subprocess.Popen('start POWERPNT C://Users//Owner//Desktop//Sample.pptx' , shell=True)