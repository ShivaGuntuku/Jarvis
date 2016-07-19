import os
import re
import time
import json
import pyautogui
import win32com.client
from win32com.client import constants
from urllib2 import Request, urlopen, URLError
from pprint import pprint

from twilio.rest import TwilioRestClient

#for speaking the voice
voiceOut = win32com.client.Dispatch('SAPI.SpVoice')


#screen shot function is here.
def screenShot():
	"""function for the taking the screen shot of current window"""
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	img_path = os.path.join(BASE_DIR,r'raw_data\screenshot')
	#print img_path
	img_name = '{0}_{1}.{2}'.format('screnshot',time.strftime('%d%m%y_%I%M%S'),'jpg')
	im1 =pyautogui.screenshot(os.path.join(img_path,img_name))
	voiceOut.Speak("your screen is successfully captured")
	return

def make_call():
	"""this function for triggering the phone call for finding the phone
	accountSid,AuthToken avilable in https://www.twilio.com/console """
	accountSid ='#####'
	authToken = '#####'
	client = TwilioRestClient(accountSid,authToken)
	call = client.calls.create(to="",  # Any phone number
						   from_="", # Must be a valid Twilio number
						   url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
	return call.sid

def get_wiki(article_title):
	"""it returns the summary of the certain wikipedia article"""
	request = Request('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+article_title)
	try:
		response = urlopen(request)
		data = json.load(response)
		#Parse the JSON to just get the extract. Always get the first summary.
		output = data["query"]["pages"]
		final = output[output.keys()[0]]["extract"]
		return final
	except URLError, e:
		print e
#print get_wiki('facebook')
