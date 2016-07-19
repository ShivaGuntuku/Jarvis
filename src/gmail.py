import time
import os
import re
import sys
import email
import base64
import smtplib
import imaplib
import feedparser
import win32com.client
from win32com.client import constants
from speech_to_text import voiceIn
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser 

voiceOut = win32com.client.Dispatch('SAPI.SpVoice')

#read the mail subject
def get_mail():
	USERNAME = ""#your email_id
	PASSWORD = ""#your Password
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])
	unreadable = 0
	if unread_count == 0 :
		voiceOut.Speak("you don't have any new mails")
	else:
		voiceOut.Speak("you have %d un-read mails"  %unread_count)
	for i in range(0,unread_count):
		try:
			print "(" + str((i+1)) + "/" + str(unread_count) + ") " + response['items'][i].title
			voiceOut.Speak(response['items'][i].title)
			time.sleep(3)
		except Exception, e:
			unreadable = unreadable+1
			continue
	if unreadable >=1:
		voiceOut.Speak("i'm sorry unable to read %d mail" %unreadable)
	return

#sending the mails
def send_mail(user,server):
	#def send_mail():
	"""Sending the mails by voice 3 arguments required
	1.to_address
	2.subject
	3.Message
	these all info you can give by voice"""
	fromaddr = '' #your email_id from this it can send the mails
	tolist = to_addrs()
	#print tolist
	sub = subj()
	#print sub
	body1 = body()
	#print body1
	msg = email.MIMEMultipart.MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = email.Utils.COMMASPACE.join(tolist)
	msg['Subject'] = sub  
	msg.attach(MIMEText(body1))
	msg.attach(MIMEText('\n\n\nsent via JarvisPython', 'plain'))
	server.sendmail(user,tolist,msg.as_string())
	voiceOut.Speak('message is sent to respected person thank you')

def to_addrs():
	voiceOut.Speak("To Address Please")
	voice = voiceIn()
	tolist = '{0}{1}'.format(voice,'@gmail.com')
	voiceOut.Speak(voice)
	return re.sub(r'\s+', '', tolist)

def subj():
	voiceOut.Speak('tell me your subject')
	voice = voiceIn()
	voiceOut.Speak('your subject is '+voice)
	return voice

def body():
	voiceOut.Speak("tell me your message")
	voice = voiceIn()
	voiceOut.Speak('your message is'+voice)
	return voice

def mail():
	user = 'guntuku.shiva@gmail.com'
	passw = 'RajuGuntuku'

	smtp_host = 'smtp.gmail.com'
	smtp_port = 587
	server = smtplib.SMTP()
	server.connect(smtp_host,smtp_port)
	server.ehlo()
	server.starttls()
	server.login(user,passw)

	imap_host = 'imap.gmail.com'
  	mail = imaplib.IMAP4_SSL(imap_host)
  	mail.login(user,passw)
  	send_mail(user,server)

#mail()

