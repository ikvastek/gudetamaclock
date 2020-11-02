from weather import *
from moonphase import *
from datetime import datetime
import os

dirname = os.path.dirname(__file__)
icon_resources = os.path.join(dirname, 'icon')

weatherid = wid()
utcsunrise = sunrise()
utcsunset = sunset()
utc = datetime.timestamp(datetime.now())
moonpath = moon_path()

def icon_path():

	if utc >= utcsunrise and utc <= utcsunset:
		if weatherid >= 200 and weatherid < 299:
			iconpath = os.path.join(icon_resources, 'thunder1.png')
		elif weatherid >= 300 and weatherid < 399:
			iconpath = os.path.join(icon_resources, 'drizzle1.png')
		elif weatherid >= 500 and weatherid < 599:
			iconpath = os.path.join(icon_resources, 'rain1.png')
		elif weatherid >= 600 and weatherid < 699:
			iconpath = os.path.join(icon_resources, 'snow1.png')
		elif weatherid >= 700 and weatherid < 799:
			iconpath = os.path.join(icon_resources, 'mist1.png')
		elif weatherid == 800:
			iconpath = os.path.join(icon_resources, 'clear1.png')
		elif weatherid == 801 or weatherid == 802:
			iconpath = os.path.join(icon_resources, 'pcloud1.png')
		elif weatherid == 803 or weatherid == 804:
			iconpath = os.path.join(icon_resources, 'cloud1.png')
		else:
			iconpath = os.path.join(icon_resources, '1.png')
	else:
		if weatherid >= 200 and weatherid < 299:
			iconpath = os.path.join(icon_resources, 'thunder2.png')
		elif weatherid >= 300 and weatherid < 399:
			iconpath = os.path.join(icon_resources, 'drizzle2.png')
		elif weatherid >= 500 and weatherid < 599:
			iconpath = os.path.join(icon_resources, 'rain2.png')
		elif weatherid >= 600 and weatherid < 699:
			iconpath = os.path.join(icon_resources, 'snow2.png')
		elif weatherid >= 700 and weatherid < 799:
			iconpath = os.path.join(icon_resources, 'mist2.png')
		elif weatherid == 800:
			iconpath = moonpath
		elif weatherid == 801 or weatherid == 802:
			iconpath = os.path.join(icon_resources, 'pcloud2.png')
		elif weatherid == 803 or weatherid == 804:
			iconpath = os.path.join(icon_resources, 'cloud2.png')
		else:
			iconpath = os.path.join(icon_resources, '2.png')
		
	return iconpath
