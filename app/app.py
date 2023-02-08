from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

load_dotenv()

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
	else:
		# for default name mathura
		city = 'London,uk'

	# your API key will come here
	api = os.getenv('API_KEY')

	# source contain json data from api
	try:
		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + api).read()
	except urllib.error.HTTPError:
		# handle 404 error
		return render_template('404.html')

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"location": str(list_of_data['name']) + ', ' + str(list_of_data['sys']['country']),
		"weather": str(list_of_data['weather'][0]['main']) + ', ' + str(list_of_data['weather'][0]['description']),
		"coordination": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
		"wind_speed": str(list_of_data['wind']['speed']) + ' m/s',
		"wind_deg": str(list_of_data['wind']['deg']) + ' deg',
		"visibility": str(list_of_data['visibility']) + ' m',
		"temperature": str(list_of_data['main']['temp']) + ' K',
		"feels_like": str(list_of_data['main']['feels_like']) + ' K',
		"temp_min": str(list_of_data['main']['temp_min']) + ' K',
		"temp_max": str(list_of_data['main']['temp_max']) + ' K',
		"pressure": str(list_of_data['main']['pressure']) + ' hPa',
		"humidity": str(list_of_data['main']['humidity']) + ' %',
		"base": str(list_of_data['base']),
	}
	return render_template('index.html', data = data)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)