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
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + api).read()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']),
		"temp": str(list_of_data['main']['temp']) + 'k',
		"pressure": str(list_of_data['main']['pressure']),
		"humidity": str(list_of_data['main']['humidity']),
	}
	print(data)
	return render_template('index.html', data = data)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)