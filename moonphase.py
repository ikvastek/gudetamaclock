import time
import requests
import os

dirname = os.path.dirname(__file__)
icon_resources = os.path.join(dirname, 'icon')

def moonphase():
	url = 'https://api.met.no/weatherapi/sunrise/2.0/.json?'

	### TO BE REPLACED ###
	lat = '45.8'
	lon = '15.9667'
	offset = '+02:00'
	### TO BE REPLACED ###
	
	date = time.strftime('%Y-%m-%d')

	query = 'lat={}&lon={}&date={}&offset={}'.format(lat,lon,date,offset)

	request = url + query
	result = requests.get(request)
	data = result.json()

	moonphaseid = data['location']['time'][0]['moonphase']['value']
	
	return moonphaseid

def moon_path():
	moonphaseid = int(float(moonphase()))

	if moonphaseid == 0:
		moonpath = os.path.join(icon_resources, 'm0.png')
	elif moonphaseid > 0 and moonphaseid <= 6:
		moonpath = os.path.join(icon_resources, 'm6.png')
	elif moonphaseid > 6 and moonphaseid <= 12:
		moonpath = os.path.join(icon_resources, 'm12.png')
	elif moonphaseid > 12 and moonphaseid <= 18:
		moonpath = os.path.join(icon_resources, 'm12.png')
	elif moonphaseid > 18 and moonphaseid <= 25:
		moonpath = os.path.join(icon_resources, 'm18.png')
	elif moonphaseid > 25 and moonphaseid <= 31:
		moonpath = os.path.join(icon_resources, 'm25.png')
	elif moonphaseid > 31 and moonphaseid <= 37:
		moonpath = os.path.join(icon_resources, 'm31.png')
	elif moonphaseid > 37 and moonphaseid <= 43:
		moonpath = os.path.join(icon_resources, 'm37.png')
	elif moonphaseid > 43 and moonphaseid <= 50:
		moonpath = os.path.join(icon_resources, 'm43.png')
	elif moonphaseid > 50 and moonphaseid <= 56:
		moonpath = os.path.join(icon_resources, 'm50.png')
	elif moonphaseid > 56 and moonphaseid <= 62:
		moonpath = os.path.join(icon_resources, 'm56.png')
	elif moonphaseid > 62 and moonphaseid <= 68:
		moonpath = os.path.join(icon_resources, 'm62.png')
	elif moonphaseid > 68 and moonphaseid <= 75:
		moonpath = os.path.join(icon_resources, 'm68.png')
	elif moonphaseid > 75 and moonphaseid <= 81:
		moonpath = os.path.join(icon_resources, 'm75.png')
	elif moonphaseid > 81 and moonphaseid <= 87:
		moonpath = os.path.join(icon_resources, 'm81.png')
	elif moonphaseid > 87 and moonphaseid <= 93:
		moonpath = os.path.join(icon_resources, 'm87.png')
	elif moonphaseid > 93 and moonphaseid < 100:
		moonpath = os.path.join(icon_resources, 'm93.png')
	else:
		moonpath = os.path.join(icon_resources, 'm100.png')
	return moonpath
