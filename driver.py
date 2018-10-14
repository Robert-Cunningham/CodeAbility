import voice_listener
import english_to_python
import keystrokes
from os import system
import time
import re
import keyboard

def callback(text, final=False):
    #concat = ' '.join([x[0] for x in phrases])
    system('clear')
    #concat = concat.replace(' exit', '')

    out = english_to_python.english_to_python(text)

    if not out:
        print("Failed.")
        return

    keystrokes.execute(out['command'], out['value'])
    #if out['command'] == 'code':
    #    subcommands = split_out_specials(out['value'])
    #    [keystrokes.execute(x['command'], x['value']) for x in subcommands]
    #else:
    #    keystrokes.execute(out['command'], out['value'])


#def split_out_specials(text):
#    sp = re.split("(\t|\n)", text)
#
#    out = [{'command': special_to_escaped(x), 'value': None} if x in specials else {'command': 'code', 'value': x} for x in sp if x != '']
#    print(out)
#
#    return out

#specials = ['\t', '\n']

#def special_to_escaped(special):
#    if special == '\n':
#        return '<newline>'
#    elif special == '\t':
#        return '<tab>'

time.sleep(2)

listener = voice_listener.Listener()
listener.listen(50, callback)
phrases = listener.getPhrases()

#keyboard.press_and_release(r'shift+;')
time.sleep(.5)


exit()