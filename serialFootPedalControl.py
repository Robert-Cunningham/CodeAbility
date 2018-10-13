import serial
import keyboard

scroll_down = 'ctrl+alt+up'
scroll_up = 'ctrl+alt+down'
tab_left = 'ctrl+shift+tab'
tab_right = 'ctrl+tab'


ser = serial.Serial("COM6", 9600)

while True:
    code=int(ser.readline())
    
    #key presses
    
    if code == 0:
        keyboard.press(scroll_down)
        print("scrolling down")

    elif code == 1:
        keyboard.press(scroll_up)
        print("scrolling up")
        
    elif code == 2:
        keyboard.press(tab_left)
        
    elif code == 3:
        keyboard.press(tab_right)
        
    #key releases

    elif code == 4:
        keyboard.release(scroll_down)

    elif code == 5:
        keyboard.release(scroll_up)
        
    elif code == 6:
        keyboard.release(tab_left)
        
    elif code == 7:
        keyboard.release(tab_right)
        
        
        
