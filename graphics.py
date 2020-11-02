import time
import os
from weather import *

dirname = os.path.dirname(__file__)
graphic_resources = os.path.join(dirname, 'graphics')

year = int(time.strftime('%Y'))
weekday = int(time.strftime('%w'))
day = str(time.strftime('%m%d'))
hour = int(time.strftime('%H'))
weatherid = wid()

def graphics_path():

	if hour == 1:
		graphicspath = os.path.join(graphic_resources, 'eggshausted.png')
	elif hour == 2:
		graphicspath = os.path.join(graphic_resources, 'bed.png')
	elif hour == 3:
		graphicspath = os.path.join(graphic_resources, 'ahhh.png')
	elif hour >= 4 and hour <= 6:
		graphicspath = os.path.join(graphic_resources, 'depressed.png')
	elif hour == 7:
		graphicspath = os.path.join(graphic_resources, 'shy.png')
	elif hour == 8:
		graphicspath = os.path.join(graphic_resources, 'tumble.png')
	elif hour == 9:
		graphicspath = os.path.join(graphic_resources, 'tired.png')
	elif hour == 10:
		graphicspath = os.path.join(graphic_resources, 'what.png')
	elif hour == 11:
		graphicspath = os.path.join(graphic_resources, 'laidback.png')
	elif hour == 12:
		graphicspath = os.path.join(graphic_resources, 'reverse.png')
	elif hour == 13:
		graphicspath = os.path.join(graphic_resources, 'shell.png')
	elif hour == 14:
		graphicspath = os.path.join(graphic_resources, 'flower.png')
	elif hour == 15:
		graphicspath = os.path.join(graphic_resources, 'chill.png')
	elif hour == 16:
		graphicspath = os.path.join(graphic_resources, 'zzz.png')
	elif hour == 17:
		graphicspath = os.path.join(graphic_resources, 'dozing.png')
	elif hour == 18:
		graphicspath = os.path.join(graphic_resources, 'meh.png')
	elif hour == 19:
		graphicspath = os.path.join(graphic_resources, 'whatever.png')
	elif hour == 20:
		graphicspath = os.path.join(graphic_resources, 'wa.png')
	elif hour == 21:
		graphicspath = os.path.join(graphic_resources, 'hood.png')
	elif hour == 22:
		graphicspath = os.path.join(graphic_resources, 'stuck.png')
	elif hour == 23:
		graphicspath = os.path.join(graphic_resources, 'handstand.png')

	else:
		graphicspath = os.path.join(graphic_resources, 'icon.png')

# Weekday

	if weekday == 5 and hour > 14 and hour <= 17:
		graphicspath = os.path.join(graphic_resources, 'friday.png')
	else:
		graphicspath = graphicspath
	
# Weathers	

	if weatherid >= 502 and weatherid <= 504:
		graphicspath = os.path.join(graphic_resources, 'brolly.png')
	elif weatherid == 602 or weatherid == 622:
		graphicspath = os.path.join(graphic_resources, 'snow.png')
	elif weatherid == 804:
		graphicspath = os.path.join(graphic_resources, 'meringue.png')
	else:
		graphicspath = graphicspath
	
# Special days

	if day == '0101':
		graphicspath = os.path.join(graphic_resources, 'ballons.png')
	elif day == '0214':
		graphicspath = os.path.join(graphic_resources, 'valentine.png')
	elif day == '0405' and year == 2021:
		graphicspath = os.path.join(graphic_resources, 'bunny.png')
	elif day == '0418' and year == 2022:
		graphicspath = os.path.join(graphic_resources, 'bunny.png')
	elif day == '0410' and year == 2023:
		graphicspath = os.path.join(graphic_resources, 'bunny.png')
	elif day == '1031' and hour > 12 and hour <= 14:
		graphicspath = os.path.join(graphic_resources, 'xray.png')
	elif day == '1031' and hour > 14 and hour <= 16:
		graphicspath = os.path.join(graphic_resources, 'boo.png')
	elif day == '1031' and hour > 16 and hour <= 18:
		graphicspath = os.path.join(graphic_resources, 'halloween.png')
	elif day == '1031' and hour > 18 and hour <= 20:
		graphicspath = os.path.join(graphic_resources, 'fairy.png')
	elif day == '1031' and hour > 20:
		graphicspath = os.path.join(graphic_resources, 'jackolantern.png')
	elif day == '1225':
		graphicspath = os.path.join(graphic_resources, 'christmas.png')
	elif day == '1004' or day == '0501' or day == '0909':
		graphicspath = os.path.join(graphic_resources, 'birthday.png')
	else:
		graphicspath = graphicspath
	
	return graphicspath
