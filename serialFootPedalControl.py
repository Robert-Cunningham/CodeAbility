import serial #from library PySerial
import keyboard

numPedals = 5
windowsSerialPort = "COM6"
linuxSerialPort = "/dev/ttyACM0"

#json_data!!
scroll_down = 'ctrl+alt+up'
scroll_up = 'ctrl+alt+down'
tab_left = 'ctrl+shift+tab'
tab_right = 'ctrl+tab'

new_line_above = 'esc+shift+o' # shift up
new_line_below = 'esc+o' # shift down

#press actions (order in array is index of pedal)

onKey = ["PTT", "SHIFT", scroll_down, scroll_up, tab_right]
onKeySHIFT = ["PTT TOGGLE", "SHIFT", new_line_below, new_line_above, tab_left] #FIX THIS

def PTTHook(a):
    pass

def setPTTHook(input_fn):
    global PTTHook
    PTTHook = input_fn

shiftState = False
PTTLockedState = False

ser = serial.Serial(windowsSerialPort, 9600)
#ser = serial.Serial(linuxSerialPort, 9600)

while True:
    code=int(ser.readline())

    #key presses

    #~~~~~~~~~~~~~~~~~~~ #when shift is OFF# ~~~~~~~~~~~~~~~~~~~~~~#
    if not shiftState:

    ######### press events ##########

        if code < numPedals:

            if onKey[code] == "PTT":
                if PTTLockedState:
                    PTTLockedState = False
                    print("Code: " + str(code) +" PTT UNLOCKED!")

                else: # if unlocked
                    print("Code: " + str(code) +" PTT ON!")
                    PTTHook(True) # send PTT on
                    ser.write(bytes(b'o')) #turn LED on


            elif onKey[code] == "SHIFT":
                shiftState = True
                print("Code: " + str(code) +" SHIFT ON!")

            else:
                keyboard.press(onKey[code])
                print("Code: " + str(code) + " " + onKey[code])

    ######### release events ##########
        else: #( when code >= numPedals)
            if onKey[code-numPedals] == "PTT":
                if PTTLockedState:
                    pass
                    #do nothing
                else: #if unlocked
                    print("Code: " + str(code) +" PTT OFF!")
                    PTTHook(False) # send PTT off
                    ser.write(bytes(b'f'))

            elif onKey[code-numPedals] == "SHIFT":
                shiftState = False
                print("Code: " + str(code) +" SHIFT OFF (already was)!")

            else:
                keyboard.release(onKey[code-numPedals])
                keyboard.release(onKeySHIFT[code-numPedals]) #to make sure shifted keys are removed too
                print("Code: " + str(code) + " " + onKey[code-numPedals] +" OFF")
                print("(and) Code: shift of " + str(code) + " " + onKeySHIFT[code-numPedals] +" OFF")


    #~~~~~~~~~~~~~~~~~~~ #when shift is ON# ~~~~~~~~~~~~~~~~~~~~~~#
    else:

    ######### press events ##########

        if code < numPedals:

            if onKeySHIFT[code] == "PTT TOGGLE":
                if PTTLockedState:
                    PTTLockedState = False
                    PTTHook(False) #send PTT off
                    print("Code: " + str(code) +" PTT UNLOCKED AND OFF!")
                    ser.write(bytes(b'f'))
                else: #if unlocked
                    PTTLockedState = True
                    PTTHook(True) #send PTT ON
                    print("Code: " + str(code) +" PTT LOCKED ON!")
                    ser.write(bytes(b'o'))

            elif onKeySHIFT[code] == "SHIFT":
                shiftState = True
                print("Code: " + str(code) +" SHIFT ON (already was)!")

            else:
                keyboard.press(onKeySHIFT[code])
                print("Code: " + str(code) + " " + onKeySHIFT[code])

    ######### release events ##########

        else: #(when code >= numPedals)
            if onKeySHIFT[code - numPedals] == "PTT TOGGLE":
                pass
                #Nothing

            elif onKeySHIFT[code - numPedals] == "SHIFT":
                shiftState = False
                print("Code: " + str(code) + " SHIFT OFF!")

            else:
                keyboard.release(onKey[code - numPedals])
                keyboard.release(onKeySHIFT[code - numPedals]) #to make sure shifted keys are removed too
                print("Code: " + str(code) + " " + onKeySHIFT[code - numPedals] +" OFF")
                print("(and) Code: normal of" + " " + str(code) + onKey[code - numPedals] +" OFF")
