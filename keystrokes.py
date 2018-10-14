import keyboard
import time
import re 


delayTime = 0

mydict = [("code","import math\na = 'abcdefg'\n"),("create","for"),('next','c'),
        ('next','a'),('next','print(c)'),('code','\nprint("...")')]

keyboard.press_and_release("ctrl+t")
keyboard.write('a')

def execute(command,input):
    if (command == 'code'):
        sp = re.split("(\t|\n|\:)", input)
        for i in sp:
            if (i == '\n'):
                keyboard.press_and_release('esc')
                keyboard.write('o')
                time.sleep(delayTime)
            elif (i == '\t'):
                keyboard.press_and_release('esc')
                keyboard.write('>>')
                keyboard.write('A')
                time.sleep(delayTime)
            elif (i == ':'):
                keyboard.press_and_release('shift+;')
                time.sleep(delayTime)
            else:
                keyboard.write(i)
                time.sleep(delayTime)
    elif (command == 'jumpline'):
        keyboard.press_and_release('esc')
        keyboard.write(str(input) + 'G')
        keyboard.press_and_release('enter')
        time.sleep(delayTime)
    elif (command == 'end_of_line'):
        keyboard.press_and_release('esc')
        keyboard.write('$')
        time.sleep(delayTime)
    elif (command == 'end_of_file'):
        keyboard.press_and_release('esc')
        keyboard.write('G')
        time.sleep(delayTime)
    elif (command == 'end_of_block'):
        keyboard.press_and_release('esc')
        keyboard.write('}')
        time.sleep(delayTime)
    elif (command == 'jumpword'):
        keyboard.press_and_release('esc')
        keyboard.write('/'+input)
        keyboard.press_and_release('enter')
        time.sleep(delayTime)
    elif (command == 'beg_of_line'):
        keyboard.press_and_release('esc')
        keyboard.write('g_')
        time.sleep(delayTime)
    elif (command == 'beg_of_file'):
        keyboard.press_and_release('esc')
        keyboard.write('gg')
        time.sleep(delayTime)
    elif (command  == 'beg_of_block'):
        keyboard.press_and_release('esc')
        keyboard.write('{')
        time.sleep(delayTime)
    elif (command == 'previous_word'):
        keyboard.press_and_release('esc')
        keyboard.write('b')
        time.sleep(delayTime)
    elif (command == 'next_word'):
        keyboard.press_and_release('esc')
        keyboard.write('e')
        time.sleep(delayTime)
    elif (command == 'back'):
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('esc')
        time.sleep(delayTime)
    elif (command == '\\t'):
        keyboard.press_and_release('esc')
        keyboard.write('>>')
        keyboard.write('A')
        time.sleep(delayTime)
    elif (command == '\\n'):
        keyboard.press_and_release('esc')
        keyboard.write('o')
        keyboard.press_and_release('esc')
        time.sleep(delayTime)
    elif (command == 'replace'):
        rel = input.split()
        keyboard.press_and_release('esc')
        keyboard.write('/'+rel[0])
        keyboard.press_and_release('enter')
        keyboard.write('ciw')
        keyboard.write(rel[1])
        keyboard.press_and_release('esc')
        time.sleep(delayTime)
    elif (command == 'create'):
        keyboard.write(input)
        time.sleep(delayTime)
    elif (command == 'next'):
        keyboard.press_and_release('tab')
        keyboard.write(input)
        time.sleep(delayTime)
    else:
        keyboard.press_and_release('esc') 
        time.sleep(delayTime)

#time.sleep(2)
#keyboard.write('a')
#for c in mydict:
 #   execute(c[0],c[1])

