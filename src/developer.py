#designer/developer info and jarvis info.
import random
from datetime import datetime
from pytz import timezone
import socket
import httplib


def devInfo():
	"""it returns the developer Information"""
	message = """ Hi I am Jarvis v2.0
	Designed and Developed by ShivaGuntuku
	he stuided B.Tech Computer Science in 2014
	currently searching for the job and while learning python programming he developed me.
	he really inspired by watching IronMan Movie Jarvis Charecter and Her Movie Samantha.
	childhood dream is develope automated voice operating system. you want to know further details about him.
	log on to shivaguntuku.github.io or find on social community's like Facebook, Twitter, Quora. 
	it's pleasure to introduce him...  Thank you."""

	return message


def aboutJarvis():
	"""it returns the information about Jarvis"""
	message = """Hi I am Jarvis v2.0
	Designed and Devloped by ShivaGuntuku 
	I am simple Voice Controlled Program i can perform more then 100 task like reading books, 
	facebook notifications,Notes writing, wheather report, time/date, joke and other specially designed tasks
	currently i'm holding 2MB of memory space, running on Windows10 Operating System with Python27 programming language.
	In futuer i am will be on github with open source and documentation. I am under the devlopement process moving toward the 
	automated voice controlled application in future until then bye. your's Jarvis v2.0
	it's pleasure to introduce him...  Thank you."""

	return message



def quotes():
	"""it returns the one of the famous quote/dailog from movies or persons"""
	quotes = ["The Starting point of all achivements is desire",
	"Don't have to, to make something special,you just have to believe it's special",
	"If you want to shine like a sun. First burn like a sun. - A.P.J Abdul Kalam ",
	"Man needs his difficulties because they are necessary to enjoy success.",
	"There is no secret ingredient",
	"Sometimes life is going to hit you in the head with a brick. Don't lose faith.",
	""" There's no perfect time for anything, do it now or you'll regret later.""",
	"""You don't need to hide yourself because you're afraid of what others think of you. 
	You have the choice to live your own life.""",
	"""Don't ever let somebody tell you you can't do something, not even me. Alright? You dream, 
	you gotta protect it. People can't do something themselves, 
	they wanna tell you you can't do it. If you want something, go get it. Period.""",
	"""You may not have your father's qualities but you will never have his weaknesses""",
	"""life is always ends up finding it's way.""",
	"""Dreams is not what you see in sleep..is the thing it doesn't let you sleep.""",
	"""success is to be measured not so much by the position that one has reached in life
	as by the obstacles he has overcome while trying to success""",
	"""what ever we learn to do, we learn by actually doing it. by Shiva""",
	"""life is a chance ,living is a choice .follow the heart future is yours.""",
	"""I may not be the best but obvious better than the one u compare me with.""",
	"Pursue excellence, and success will follow",
	""" success, like a happiness ,can not pursued, it must ensue.""",
	"""Everything fair in Love and War..""",
	"""if you fail to prepare, you prepare to fail.""",
	"""success is getting what u want, happiness is wanting what you get.""",
	"""persistence is the mother of personal change.""",
	"""life is opportunity to achieve something.....  __Praveen Pal""",
	"""When I started earning, I came to know My never ending wishes were fulfilled by 
	my parents money,With my money, I can only buy stuff that is really needed""",
	"""It's never too late to start over. If you weren't happy with yesterday, try something different today. 
	Don't stay stuck. Do better.""",
	"""Believe in yourself. Your confidence will lead you to success and happiness.""",
	"Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called present.",
	]

	return random.choice(quotes)
#print quotes()
def jokes():
	"""It tells the random joke """
	jokes = [
		"""What do beggars and software engineers have in common? They both ask the same question when 
	meeting another one of their kind; Which platform are you working on?""",
		"""sql DELETE FROM world.human_race WHERE iq less than 100 Query OK, 3.45 billion rows affected 0.01 sec""",
		"""A man is smoking a cigarette and blowing smoke rings into the air. His girlfriend becomes irritated 
	with the smoke and says, Can't you see the warning on the cigarette pack? Smoking is hazardous to your 
	health!' To which the man replies, I am a bad programmer. We don't worry about warnings; we only worry about errors.""",
		""" I am not a vegetarian because I love animals. I am a vegetarian because I hate plants""",
 #        """A year ago I upgraded from Girlfriend 7.0 to Wife 1.0 and I have observed that this new program 
	# started an unexpected subroutine called Son, which occupies almost all my space and important resources. 
	# Also, Wife 1.0 auto-installs as a host in all my programs and auto-starts every time I want to use any of 
	# them. Apps like Beers With Friends 10.3 and Sunday Football 5.0 no longer work.
	# Every now and then, a spyware program called In-Law 1.0 starts and freezes Wife 1.0. I haven't been able 
	# to uninstall this spyware and I cannot minimize Wife 1.0 if I want to run any of my favorite apps. 
	# I'm thinking about downgrading to Girlfriend 7.0 but uninstall IS NOT WORKING!!! Please Help!!
	# SUPPORT RESPONSE:
	# Dear User:
	# This is a known bug submitted by users. In most cases the source is pretty simple. Many users go from 
	# version Girlfriend X.0 to Wife 1.0 thinking Wife 1.0 is an utilities and entertainment app. However, 
	# Wife 1.0 is designed to control the system entirely. It is very unlikely that you'll be able to uninstall
	# Wife 1.0 and return to any version of Girlfriend. There are hidden files on Girlfriend X.0 that will 
	# make it work just like Wife 1.0.
	# Some users have tried clean formatting their systems in order to install Girlfriend Plus 1.0 or Wife 2.0 
	# but ended with bigger problems afterwards. Please refer to the warning section on the read-me file, 
	# specifically the alimony chapter.
	# Also, if you update to Girlfriend 8.0, do not update to Wife 2.0 because problems will be worst, 
	# expensive and not recommended for normal users. Frequently used upgrades include Celibacy 1.0 or 
	# Gay/Lesbian 5.3.
	# I personally have Wife 1.0 installed and suggest you explore the manual in its entirety. 
	# The user agreement states that the user shall be responsible for any problem, no matter the cause. 
	# A really powerful command, which normally un-freezes the application can be found under 
	# C:/IMSORRY.EXE. Having said that, Wife 1.0 is really interesting but has very expensive updates. 
	# Recommended plugins include Flowers 12.0, Jewels 2.3 and Vacations 2.3. Yeshoney 9.0 and Whateveryousay 
	# 12.3 are also very popular.
	# Finally, Wife 1.0 is not compatible with MiniSkirtSecretary 3.3. 
	# Installing it can cause irreversible damage to the operating system.""",
		"""Wife:
	Today, I want to relax,
	so I have brought three movie tickets.
	Husband: why three tickets?
	Wife: you and your parents.
	""" ]

	return random.choice(jokes)

def currentTime(): 
	"""function for current time """
	india = timezone('Asia/Kolkata')
	IN_time = datetime.now(india)
	#print sa_time.strftime('%Y-%m-%d_%H-%M-%S')
	return IN_time.strftime('%I hours %M minutes %S seconds %p %A %d %B %Y')


def machine_info():
	"""it returns the machine name and IP address"""
	return socket.gethostname()
	#return socket.gethostbyname(socket.gethostname())

def have_internet():
	"""It returns the internet connected or not"""
	conn = httplib.HTTPConnection("www.google.com")
	try:
		conn.request("HEAD", "/")
		return "Internet is Connected"
	except:
		return "Internet Not Connected"

