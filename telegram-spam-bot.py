import pyautogui, time, datetime
  
time.sleep(2)
  
while True:
    
    # to display the time at which the message is sent 
    print(datetime.datetime.now())
    pyautogui.typewrite("WAKE UP") 
    pyautogui.press("enter")
    time.sleep(1)
  
    print(datetime.datetime.now())