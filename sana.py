import keyboard
import time

mydict = {"code":"import","jumpline":"12"}

time.sleep(2)
keyboard.press_and_release('ctrl+t')

def execute(command,input):
    time.sleep(2)
    if command == 'code':
        keyboard.write('i')
        keyboard.write(input)
        keyboard.press_and_release('esc')
    elif command == 'jumpline':
        keyboard.write(':' + input + 'G') 

for c,v in mydict.items():
    execute(c,v)
    time.sleep(2)