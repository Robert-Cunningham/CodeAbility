import voice_listener
import english_to_python
import sana
from os import system
import time
import re
import keyboard

def callback(text):
    #concat = ' '.join([x[0] for x in phrases])
    system('clear')
    print(text)
    #concat = concat.replace(' exit', '')

    out = english_to_python.english_to_python(text.strip())
    print('attempting to write', out)

    if out['command'] == 'code':
        subcommands = split_out_specials(out['value'])
        [sana.execute(x['command'], x['value']) for x in subcommands]
    else:
        sana.execute(out['command'], out['value'])


def split_out_specials(text):
    sp = re.split("(\t|\n)", text)

    out = [{'command': special_to_escaped(x), 'value': None} if x in specials else {'command': 'code', 'value': x} for x in sp if x != '']
    print(out)

    return out

specials = ['\t', '\n']

def special_to_escaped(special):
    if special == '\n':
        return '<newline>'
    elif special == '\t':
        return '<tab>'

print(split_out_specials('asdf\tfjs\n'))

time.sleep(2)

callback("if 7 equals 6 then return 3")

#listener = voice_listener.Listener()
#listener.listen(5, callback)
#phrases = listener.getPhrases()

keyboard.press_and_release(r'shift+;')
time.sleep(.5)


exit()