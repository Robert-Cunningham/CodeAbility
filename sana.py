import keyboard
import time

keyboard.press_and_release('ctrl+t')
time.sleep(.5)

def execute(command,input):
    try:
        if (command == 'code'):
            keyboard.press_and_release('i')
            keyboard.write(input)
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
        elif (command == '<tab>'):
           keyboard.press_and_release('tab')
        elif (command == '<newline>'):
            keyboard.press_and_release('enter')
        else:
            keyboard.press_and_release('esc') 
    except:
        pass
    time.sleep(.5)