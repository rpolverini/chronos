# python script that make sounds when your battery is low
import psutil
import pygame
import os

# Configuration
archivoTestigo='archbat.txt'
sonido= "/usr/share/sounds/gnome/default/alerts/TF050.WAV"
limiteBateria = 25


os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'
home = os.path.expanduser('~')
# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
# returns a tuple
battery = psutil.sensors_battery()
  
print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)
print("Home:", home)  
# converting  seconds to hh:mm:ss
print("Battery left : ", convertTime(battery.secsleft))

file = open(home + '/'+ archivoTestigo, 'w')
file.write(str(battery.percent))
if battery.percent <limiteBateria and not battery.power_plugged:
	pygame.mixer.init()
	pygame.mixer.music.load(sonido)
	for x in range(0,3):
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
	print("Fin")
