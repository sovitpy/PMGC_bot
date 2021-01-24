import pyautogui
import time

#Countdown Module Definition
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

#Main Block
print("Sleeping for 10 seconds.. Point your cursor to the YouTube Chat Box")
countdown(10)
print("Starting the bot...\n\n")
n = 0
while True:
    n += 1
    pyautogui.write('#PMGCxOnePlus',interval=0.25)
    time.sleep(1)
    pyautogui.press("enter")
    print(f"Sent!\nTotal hashtags sent: {n}")
    print("Sending again in(slowmode cooldown):")
    countdown(60)
    print("\n\n")