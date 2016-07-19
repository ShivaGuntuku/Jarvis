#changing the background image of desktop
import ctypes
import os
import random
import ast
import scandir

#basedir location,config file you have to edit where the wallpapers are stored
Base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
config_file = os.path.join(Base_dir,'raw_data','.config')

with open(config_file,'r') as f :
	images=[]
	for p in ast.literal_eval(f.read()).values():
		for file in os.listdir(p):
			images.append(os.path.join(p,file))
	for img in random.sample(images,len(images)):
		#img= '{0}"{1}"'.format('r',img)
		#print img
		break
		
	
def bg_img():	
	"""This function for changing wallpaer which collected from the harddrive"""		
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 
		0, 
		img, 
		3)

#bg_img()