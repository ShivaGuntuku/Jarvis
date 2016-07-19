import random
import mp3play
import os
import scandir
import time
from mutagen.mp3 import MP3
from math import floor

def mp3files():
	"""collecting the media(mp3) files from HDD
	other wise you can put mp3 files in the raw_data folder"""
	Base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
	mp3_source = os.path.join(Base_dir,'raw_data','mp3_files')
	mp3list = []
	for paths,dirs,files in scandir.walk(mp3_source):
	#for paths,dirs,files in scandir.walk(r'D:\Audio\forJarvis'):
		"""if want to search mp3 files from all you HDD then 
		provide all drives path postions instead of D:\\Audio
		add extra back slash where ever back slash occur. 
		"""
		for file in files:
			if file.endswith('.mp3'):
				fullpath =mp3list.append(os.path.join(paths,file))
	#print mp3list
	#print len(mp3list)
	return mp3list
#mp3files()


def length(file):
	"""This function main role is find the time length of Mp3 file """
	audio = MP3(file)
	return audio.info.length


def playFile():
	"""function role is to play the random music files collected from
	HDD"""

	mp3list = mp3files()  # collected mp3 files list
	count = len(mp3list)
	for i in random.sample(mp3list, count):
		print i  # which file is played
		clip = mp3play.load(i)
		clip.play()
		filelength = length(i)
		# Let it play for up to 30 seconds, then stop it.
		time.sleep(min(filelength, clip.seconds()))
		clip.stop()

#playFile()  # for testing process script is working or not.
