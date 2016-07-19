
import pyaudio
import wave
import sys
import os

CHUNK = 1024
Base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
file_name = os.path.join(Base_dir,'raw_data','beep_hi.wav')
#print file_name


def wavPlay(file_name):
	"""this script will play the .wav file"""
	wf = wave.open(file_name, 'rb')

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

	data = wf.readframes(CHUNK)

	while data != '':
    		stream.write(data)
    		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()
#wavPlay(file_name)