import serial
import keyboard
import time

scroll_down = 'ctrl+alt+up'
scroll_up = 'ctrl+alt+down'
tab_left = 'ctrl+shift+tab'
tab_right = 'ctrl+tab'

doubleDelay = 700
lastCodeTime = 0
lastCode = -1

ser = serial.Serial("COM6", 9600)

while True:
    =int(ser.readline())
    currentTime = int( round(time.time() * 1000) )
    
    print("EVENT! CODE:" + str(code)+ " LAST CODE: " + str(lastCode) + " CURRENT TIME: " + str(currentTime) + "lastCodeTime: "+ str(lastCodeTime))

    
    #key presses
    
    if code == 0:
        if lastCode == code and (currentTime - lastCodeTime) < doubleDelay :
            print("double click!")
        else:
            keyboard.press(scroll_down)
            print("single click")

    elif code == 1:
        keyboard.press(scroll_up)
        
        
    elif code == 2:
        keyboard.press(tab_left)
        
    elif code == 3:
        keyboard.press(tab_right)
        
    #key releases

    elif code == 4:
        keyboard.release(scroll_down)
        print("released")

    elif code == 5:
        keyboard.release(scroll_up)
        
    elif code == 6:
        keyboard.release(tab_left)
        
    elif code == 7:
        keyboard.release(tab_right)

    if code in [0,1,2,3]:
        lastCode = code
    
    lastCodeTime = currentTime
        
        
        
