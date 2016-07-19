import os
import re
import sys
import random

import win32com.client
from win32com.client import constants
from src.speech_to_text import voiceIn

from src.wav import wavPlay
from src.change_bgimg import bg_img
from src.dark_light import light_dark
from src.developer import devInfo,aboutJarvis,quotes,jokes,currentTime,have_internet,machine_info
from src.gmail import get_mail,mail
from src.music_player import playFile
from src.simpleScript import screenShot,make_call,get_wiki

voiceOut = win32com.client.Dispatch('SAPI.SpVoice')



while True:
	voice = voiceIn()
	if voice == None:
		voiceOut.Speak("microphone not connected or device problem")
		sys.exit(0)
	elif bool(re.search(r'\bjarvis\b', voice, re.IGNORECASE)):
		wavPlay(r'H:\SamanthaV1.2\beep_hi.wav')

	voiceOut.Speak("Hello Shiva., how can i help you")
	voice=voiceIn()
	voiceOut.Speak ('recognizing it..')

	if bool(re.search(r'\bmusic|songs|tracks\b', voice, re.IGNORECASE)):
		voiceOut.Speak ("playing Songs wait.")
		playFile()


	elif bool(re.search(r'\bwiki|info|wikipedia\b', voice, re.IGNORECASE)):
		voiceOut.Speak('give me a word or name for knowing the info ')
		voice_wiki=voiceIn()
		voiceOut.Speak('your word is'+ voice_wiki +'is it right shiva')
		wili_result=get_wiki(voice_wiki)
		voiceOut.Speak(wili_result)

	elif bool(re.search(r'\btime\b', voice, re.IGNORECASE)):
		time = currentTime()
		voiceOut.Speak(time)

	elif bool(re.search(r'\bbore|joke|smile|laugh|not interest\b', voice, re.IGNORECASE)):
		laugh = jokes()
		voiceOut.Speak(laugh)

	elif bool(re.search(r'\bdevInfo|Author|creator|designer\b', voice, re.IGNORECASE)):
		messages = devInfo()
		voiceOut.Speak(messages)

	elif bool(re.search(r'\babout you|speak engine|idiot\b', voice, re.IGNORECASE)):
		messages = aboutJarvis()
		voiceOut.Speak(messages)

	elif bool(re.search(r'\btake a pic|picture|camera|photo\b', voice, re.IGNORECASE)):
		from source.camera import take_pic
		take_pic()
		voiceOut.Speak('your picture is saved')

	elif bool(re.search(r'\bcan i go outside|light|dark|sunrice\b', voice, re.IGNORECASE)):
		messages = light_dark()
		voiceOut.Speak(messages)

	elif bool(re.search(r'\bscreenshot|print|screen|save\b', voice, re.IGNORECASE)):
		messages = screenShot()
		voiceOut.Speak(messages)

	elif bool(re.search(r'\bfind|phone|trigger|call\b', voice, re.IGNORECASE)):
		make_call()
		voiceOut.Speak('wait for a moment..')

	elif bool(re.search(r'\bread email|email|gmail|notifications\b', voice, re.IGNORECASE)):
		get_mail()
		#voiceOut.Speak('wait for a moment..')

	elif bool(re.search(r'\bsend mail|outbox|send\b', voice, re.IGNORECASE)):
		mail()
		#voiceOut.Speak('wait for a moment..')

	elif bool(re.search(r'\binterent status|connectivity\b', voice, re.IGNORECASE)):
		messages = have_internet()
		voiceOut.Speak(messages)

	elif bool(re.search(r'\bstop|exit|terminate|close\b', voice, re.IGNORECASE)):
		voiceOut.Speak("excution will be stoped in moment..")
		sys.exit(0)		

	elif bool(re.search(r'\bfacebook|fb|face book\b', voice, re.IGNORECASE)):
		os.startfile("http://www.facebook.com")

	elif bool(re.search(r'\bgoogle|search\b', voice, re.IGNORECASE)):
		os.startfile("http://www.google.com")

	elif bool(re.search(r'\bwallpaper|desktop\b', voice, re.IGNORECASE)):
		bg_img()
		voiceOut.Speak("desktop image is changed checkout")
		
	else :
		messages = ["I'm sorry, could you repeat that?",
				"My apologies, could you try saying that again?",
				"Say that again?", "I beg your pardon?"]
		voiceOut.Speak(random.choice(messages))
