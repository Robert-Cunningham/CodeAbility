import keyboard
import time

mydict = {"code":"import","jumpline":"12"}

def execute(command,input):
    if command == 'code':
        keyboard.write('i')
        keyboard.write(input)
        keyboard.press_and_release('esc')
    elif (command == 'jumpline'):
        keyboard.write(':' + input + 'G') 

for c in mydict:
    execute(c,mydict[c])

