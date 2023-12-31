from flask import Flask, render_template, request
import requests

# import json

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/weatherapp", methods=['POST', 'GET'])
def get_watherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": request.form["city"],
        "appid": request.form["appid"],
        "units": request.form["units"]
    }
    weather_data = requests.get(url, params=params)
    weather_data_json = weather_data.json()
    city = weather_data_json['name']
    temp_min = weather_data_json['main']['temp_min']
    temp_max = weather_data_json['main']['temp_max']

    return f"""temp_range for {city} with min of {temp_min} and max of {temp_max} 
    the complete weather data is mentioned below </br> {weather_data_json}"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")  # type: ignore
