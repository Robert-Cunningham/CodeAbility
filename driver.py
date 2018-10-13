import voice_listener
import english_to_python

def callback(data):
    print('data', data)

listener = voice_listener.Listener()
listener.listen(5, callback)
phrases = listener.getPhrases()

concat = ' '.join([x[0] for x in phrases])
print(concat)
concat = concat.replace(' exit', '')
print(english_to_python.english_to_python(concat))

exit()