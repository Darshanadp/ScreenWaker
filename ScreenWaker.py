import notifypy
# import pyautogui
import time
import threading
from pynput.keyboard import Key, Controller
import datetime

#timming variables
notifybefore = 60 #nofication popup before 10s the program close (default value = 60s)
intervaldefault = 10*60 #inverval between two curser changes (default value = 15*60s)
x = 683 # X - cordination for curser changes (default value = 683)
chay = 40 # how much want to change y cordination (default value = 40)

#notification 
bubble = notifypy.Notify()
bubble.title = "Timer Ran Out"
bubble.message = f"Your screen awaker program about to finished it's job in less than {notifybefore} seconds!!! :)"


#system variable
checking = True
fin = 0
keyboard = Controller()


def checkingtime():
    global fin
    checkbubble = False

    while checking == True:
        if fin >= interval:
            fin = 0
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        if secTime <= notifybefore and checkbubble == False:
                checkbubble = True
                bubble.send()
        time.sleep(0.1)

def timer():
    global fin
    global secTime
    global checking

    while secTime > 0:
        print(f"Timer : {secTime:03.0f} second(s)",end='\r')
        secTime = secTime - 1
        fin = fin + 1
        time.sleep(1)
    else:
        checking = False
        now = datetime.datetime.now()
        print(f"Timer is Turned off after {setTime} minute(s) by the System")
        print("The Timer stopped at", now.strftime("%H:%M:%S"))
        print("\nPress ENTER to exit the program")
        input()
            

timer_thread = threading.Thread(target=timer)
checkingtime_thread = threading.Thread(target=checkingtime)

if __name__ == "__main__":
    global setTime
    global secTime
    print("============== All the value should in miniutes =============\n")
    setTime = float(input("Enter Screen Wake Up Time : "))
    intert = (input("Enter Interval Time (Press Enter to set defalut value 10min) : "))
    if intert == "":
        interval = intervaldefault
    else:
        interval = float(intert) * 60
    print("-------------------------------------------------------------")
    secTime = setTime * 60

    timer_thread.start()
    checkingtime_thread.start()


    
    
    
    

    
