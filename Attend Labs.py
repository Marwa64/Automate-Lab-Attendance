import webbrowser
import pynput.mouse
from pynput.mouse import Button, Controller
import keyboard
import schedule
import time
import pyautogui

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
nameAndID = ''

i = 1

advancedOS = 'https://eu.bbcollab.com/collab/ui/session/guest/566e6336815c400fb82b16664f8a5659'
graphics = 'https://eu.bbcollab.com/collab/ui/session/guest/0bef3ac5648845f8a747a6a2e40ca1ef'
concepts = 'https://eu.bbcollab.com/collab/ui/session/guest/cc52e24eae9146289f26a2c1358dce9a'

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'lab ' + str(i) + '.jpg')

def attendLab(url:str):

    webbrowser.get(chrome_path).open(url)

    mouse = Controller()
    positions = ((768, 512),(354, 437),(314, 252),(594, 536),(862, 369),(1154, 600),(1277, 44),(898, 411))

    time.sleep(20)

    keyboard.write(nameAndID)

    submitName = (540, 650)
    mouse.position = submitName
    time.sleep(3)
    mouse.click(Button.left,1)

    time.sleep(20)

    closeAudioTest = (1250,85)
    mouse.position = closeAudioTest
    time.sleep(3)
    mouse.click(Button.left,1)

    takeScreenshot()
    i += 1
    
    time_sleep = (10, 20, 500, 30, 1000, 20, 15, 15, 1000)
    i = 0
    for position in positions:
        sec = time_sleep[i]
        mouse.position = position
        time.sleep(sec)
        i+=1
        if i>= len(positions):
            break

schedule.every().sunday.at("12:25").do(attendLab, advancedOS)
schedule.every().monday.at("08:40").do(attendLab, graphics)
schedule.every().monday.at("10:10").do(attendLab, concepts)

while True:
    schedule.run_pending()
    time.sleep(10)
