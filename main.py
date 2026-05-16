import os
import requests
from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None
    error_msg = None
    city_time = None
    city_date = None

    API_KEY = os.environ.get("WEATHER_API_KEY")

    if request.method == 'POST':
        city = request.form.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                
                timezone_offset = weather_data.get('timezone', 0) # seconds mein
                utc_time = datetime.utcnow()
                local_target_time = utc_time + timedelta(seconds=timezone_offset)
                
                city_time = local_target_time.strftime("%I:%M %p") # E.g., 04:30 PM
                city_date = local_target_time.strftime("%A, %B %d, %Y") # E.g., Saturday, May 16, 2026
                
                weather_data['sys']['sunrise_time'] = (datetime.utcnow() + timedelta(seconds=timezone_offset)).strftime("%I:%M %p")
                weather_data['sys']['sunset_time'] = (datetime.utcnow() + timedelta(seconds=timezone_offset)).strftime("%I:%M %p")

            else:
                error_msg = "Sheher ka naam sahi nahi hai, please check karein!"
        except Exception as e:
            error_msg = "Server connect nahi ho pa raha hai."

    return render_template('index.html', weather=weather_data, city=city, error=error_msg, city_time=city_time, city_date=city_date)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))