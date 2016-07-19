import speech_recognition as sr
import win32com.client
from win32com.client import constants

voiceOut = win32com.client.Dispatch('SAPI.SpVoice')

def voiceIn():
	"""work like microphone"""
	try:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			#voiceOut.Speak('say something')
			audio = r.listen(source)
			try:
				return  r.recognize_google(audio)
			except LookupError:
				voiceOut("Could not understand audio")
	except Exception, e:
		pass
		#return "you're input device not recognized" 

#s= voiceIn()
#voiceOut.Speak(s)