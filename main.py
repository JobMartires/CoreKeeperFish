import pyautogui
import time

pyautogui.useImageNotFoundException()

def main():
    catch = 1
    searchRegion = (900, 350, 200, 200)

    while True:
        try:
            bite = pyautogui.locateOnScreen("trigger.png", region=searchRegion, confidence=0.9)

            if bite:
                #reel in fish
                pyautogui.click(button='right')
                print('Catch #', catch)
                catch += 1
                #recast
                time.sleep(2)
                pyautogui.click(button='right')
            else:
                continue

        except pyautogui.ImageNotFoundException:
            continue
main()


        