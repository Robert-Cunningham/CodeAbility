import voice_listener
import english_to_python
from os import system

def callback(text):
    #concat = ' '.join([x[0] for x in phrases])
    system('clear')
    print(text)
    #concat = concat.replace(' exit', '')
    print(english_to_python.english_to_python(text))

listener = voice_listener.Listener()
listener.listen(5, callback)
phrases = listener.getPhrases()


exit()