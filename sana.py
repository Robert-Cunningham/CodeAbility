import keyboard
import time

mydict = {"code":"import","jumpline":"12"}

keyboard.press_and_release('ctrl+t')

def execute(command,input):
    print(command, input)
    try:
        if command == 'code':
            keyboard.write('i')
            keyboard.write(input)
            keyboard.press_and_release('esc')
        elif command == 'jumpline':
            keyboard.write(':' + input + 'G') 
    except:
        pass
    time.sleep(.5)