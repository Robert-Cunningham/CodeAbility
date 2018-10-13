import keyboard
import time
import re 


dict = {"code":"import code:\nnext line\tthird line\t\n()"}

def execute(command,input):
    time.sleep(2)
    if (command == 'code'):
        keyboard.write('a')
        sp = re.split("(\t|\n|\:)", input)
        for i in sp:
            if (i == '\n'):
                keyboard.press_and_release('enter')
            elif (i == '\t'):
                keyboard.press_and_release('esc')
                keyboard.write('>>')
                keyboard.write('A')
                time.sleep(0.5)
            elif (i == ':'):
                keyboard.write(':')
            else:
                keyboard.write(i)
        keyboard.press_and_release('esc')
    elif (command == 'jumpline'):
        keyboard.write(input + 'G')
        keyboard.press_and_release('enter')
    elif (command == 'end_of_line'):
        keyboard.write('$')
    elif (command == 'end_of_file'):
        keyboard.write('G')
    elif (command == 'end_of_block'):
        keyboard.write('}')
    elif (command == 'jumpword'):
        keyboard.write('\\'+input)
        keyboard.press_and_release('enter')
    elif (command == 'beg_of_line'):
        keyboard.write('g_')
    elif (command == 'beg_of_file'):
        keyboard.write('gg')
    elif (command  == 'beg_of_block'):
        keyboard.write('{')
    elif (command == 'last_word'):
        keyboard.write('b')
    elif (command == 'next_word'):
        keyboard.write('e')
    elif (command == 'back'):
        keyboard.press_and_release('backspace')
    elif (command == '\\t'):
       keyboard.press_and_release('tab')
    elif (command == '\\n'):
        keyboard.press_and_release('enter')
    else:
        keyboard.press_and_release('esc') 

