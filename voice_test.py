from __future__ import division

import re
import sys
import keyboard

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

RATE = 16000
CHUNK = int(RATE / 10)	# 100ms
phrases = []

class MicrophoneStream(object):
	def __init__(self, rate, chunk):
		self.rate = rate
		self.chunk = chunk

		self.buff = queue.Queue()
		self.closed = True

	def __enter__(self):
		self.audio_interface = pyaudio.PyAudio()
		self.audio_stream = self.audio_interface.open(
			format=pyaudio.paInt16,
			channels=1, rate=self.rate,
			input=True, frames_per_buffer=self.chunk,
			stream_callback=self.fill_buffer
		)
		self.closed = False
		return self

	def __exit__(self, type, value, traceback):
		self.audio_stream.stop_stream()
		self.audio_stream.close()
		self.closed = True
		self.buff.put(None)
		self.audio_interface.terminate()

	def fill_buffer(self, in_data, frame_count, time_info, status_flags):
		self.buff.put(in_data)
		return None, pyaudio.paContinue

	def generator(self):
		while not self.closed:
			chunk = self.buff.get()
			if chunk is None:
				return
			data = [chunk]

			while True:
				try:
					chunk = self.buff.get(block=False)
					if chunk is None:
						return
					data.append(chunk)
				except queue.Empty:
					break

			yield b''.join(data)

	def listen_print_loop(self, responses):
		num_chars_printed = 0
		for response in responses:
			if not response.results:
				continue

			result = response.results[0]
			if not result.alternatives:
				continue

			transcript = result.alternatives[0].transcript

			overwrite_chars = ' ' * (num_chars_printed - len(transcript))

			if not result.is_final:
				sys.stdout.write(transcript + overwrite_chars + '\r')
				sys.stdout.flush()
				num_chars_printed = len(transcript)
			else:
				sys.stdout.write(transcript + overwrite_chars + '\r')
				phrases.append(transcript)
				if re.search(r'\b(exit|quit)\b', transcript, re.I):
					print("exiting...")
					break
				print('\n')
				num_chars_printed = 0

def main():
	language_code = 'en-US'
	print('Switch to the file you wish to write to then begin talking...')
	client = speech.SpeechClient()
	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
		sample_rate_hertz=RATE,
		language_code=language_code)
	streaming_config = types.StreamingRecognitionConfig(
		config=config,
		interim_results=True)

	with MicrophoneStream(RATE, CHUNK) as stream:
		audio_generator = stream.generator()
		requests = (types.StreamingRecognizeRequest(audio_content=content)
			for content in audio_generator)

		responses = client.streaming_recognize(streaming_config, requests)

		stream.listen_print_loop(responses)

	print(phrases)

if __name__ =='__main__':
	main()
