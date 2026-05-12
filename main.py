import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Aapki API Key yahan set hai
API_KEY = "3716b0aee2851aa802b22bef0dc81b71"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None
    error_msg = None

    if request.method == 'POST':
        city = request.form.get('city')
        # units=metric ka matlab hai temperature Celsius mein aayega
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_msg = "City nahi mili, please naam sahi likhein!"
        except Exception as e:
            error_msg = "Kuch error aaya, baad mein try karein."

    return render_template('index.html', weather=weather_data, city=city, error=error_msg)

if __name__ == "__main__":
    # Cloud Run ke liye port 8080 zaroori hai
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))