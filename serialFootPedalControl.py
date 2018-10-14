import serial
import keyboard
import time

numPedals = 5

scroll_down = 'ctrl+alt+up'
scroll_up = 'ctrl+alt+down'
tab_left = 'ctrl+shift+tab'
tab_right = 'ctrl+tab'

#press actions (order in array is index of pedal)

onKey = ["PTT", "SHIFT", scroll_down, scroll_up, tab_right]
onKeySHIFT = ["PTT TOGGLE"] #FIX THIS
              
shiftState = False

ser = serial.Serial("COM6", 9600)

while True:
    code=int(ser.readline())
    
    #key presses

    #~~~~~~~~~~~~~~~~~~~ #when shift is OFF# ~~~~~~~~~~~~~~~~~~~~~~#
    if not shiftState:
	    
	######### press events ##########
	    
        if code < numPedals: 
              
            if onKey[code] == "PTT":
                print("Code: " + str(code) +" PTT ON!")
                #insert extra function here
                  
            elif onKey[code] == "SHIFT":
                shiftState = True
                print("Code: " + str(code) +" SHIFT ON!")
                  
            else:
                keyboard.press(onKey[code])
                print("Code: " + str(code) + " " + onKey[code])

	######### release events ##########
        
        else: 
            if onKey[code-numPedals] == "PTT":
                print("Code: " + str(code) +" PTT OFF!")
                #insert extra function here
                  
            elif onKey[code-numPedals] == "SHIFT":
                shiftState = False
                print("Code: " + str(code) +" SHIFT OFF (already was)!")
                  
            else:
                keyboard.release(onKey[code-numPedals]) 
                #keyboard.release(onKeySHIFT[code-numPedals]) #to make sure shifted keys are removed too #REMOVED UNTIL SHIFT FIXED!!!!!
                print("Code: " + str(code) + " " + onKey[code-numPedals] +" OFF")
                #print("(and) Code: shift of " + str(code) + " " + onKeySHIFT[code-numPedals] +" OFF")
                
            
    #~~~~~~~~~~~~~~~~~~~ #when shift is ON# ~~~~~~~~~~~~~~~~~~~~~~#    
    else: 

	######### press events ##########
        
        if code < 5:
              
            if onKeySHIFT[code] == "PTT":
                print("Code: " + str(code) +" PTT ON!")
                #insert extra function here
                  
            elif onKeySHIFT[code] == "SHIFT":
                shiftState = True
                print("Code: " + str(code) +" SHIFT ON (already was)!")
                  
            else:
                keyboard.press(onKeySHIFT[code])
                print("Code: " + str(code) + " " + onKeySHIFT[code])

	######### release events ##########
        
        else:
            if onKey[code - numPedals] == "PTT":
                print("Code: " + str(code) +" PTT OFF!")
                #insert extra function here
                  
            elif onKey[code - numPedals] == "SHIFT":
                shiftState = False
                print("Code: " + str(code) + " SHIFT OFF!")
                  
            else:
                keyboard.release(onKey[code - numPedals]) #maybe remove to PURPOSELY stick keys
                keyboard.release(onKeySHIFT[code - numPedals]) #to make sure shifted keys are removed too
                print("Code: " + str(code) + " " + onKeySHIFT[code - numPedals] +" OFF")
                print("(and) Code: normal of" + " " + str(code) + onKey[code - numPedals] +" OFF")
        
        
        
