import voice_listener
import english_to_python
import sana
from os import system
import time

def callback(text):
    #concat = ' '.join([x[0] for x in phrases])
    system('clear')
    print(text)
    #concat = concat.replace(' exit', '')

    code = english_to_python.english_to_python(text)
    print('attempting to write', code)
    sana.execute('code', code)

time.sleep(2)

listener = voice_listener.Listener()
listener.listen(5, callback)
phrases = listener.getPhrases()


exit()