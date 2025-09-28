from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nltk
import spacy
from transformers import pipeline
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# NLP setup
nltk.download('punkt')
nltk.download('punkt_tab')
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")

# OpenWeatherMap API
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/"

if not API_KEY:
    raise ValueError("OPENWEATHERMAP_API_KEY environment variable not set!")

# Utility functions
def get_icon_url(icon):
    return f"https://openweathermap.org/img/wn/{icon}@2x.png"

def get_current_temperature(lat=None, lon=None, city_name=None):
    if city_name:
        url = f"{BASE_URL}weather?q={city_name}&units=metric&appid={API_KEY}"
    elif lat is not None and lon is not None:
        url = f"{BASE_URL}weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    else:
        return None

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'name': data['name'],
            'icon': get_icon_url(data['weather'][0]['icon']),
            'description': data['weather'][0]['description']
        }
    return None

def get_forecast(lat=None, lon=None, city_name=None):
    if city_name:
        url = f"{BASE_URL}forecast?q={city_name}&units=metric&appid={API_KEY}"
    elif lat is not None and lon is not None:
        url = f"{BASE_URL}forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    else:
        return None, None

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecasts = {}
        for item in data['list']:
            day_name = datetime.fromtimestamp(item['dt']).strftime('%A')
            if day_name not in forecasts:
                forecasts[day_name] = []
            forecasts[day_name].append({
                'datetime': datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M'),
                'temp': item['main']['temp'],
                'humidity': item['main']['humidity'],
                'icon': get_icon_url(item['weather'][0]['icon']),
                'description': item['weather'][0]['description']
            })
        return forecasts, data['city']['name']
    return None, None

def generate_recommendation(description):
    desc = description.lower()
    if 'rain' in desc:
        return "It will rain, take an umbrella 🌂."
    elif 'clear' in desc:
        return "The weather is clear, wear sunglasses 😎."
    elif 'snow' in desc:
        return "It will snow, wear warm clothes ❄️."
    else:
        return "Weather seems normal, have a great day ☀️!"

# --- IMPROVED CITY EXTRACTION ---
def extract_city(query):
    """
    Extracts city/state name using spaCy NER or fallback to proper nouns after keywords,
    ignoring filler words like 'for', 'in', 'at', 'the', 'of'.
    """
    filler_words = ['for', 'in', 'at', 'the', 'of']
    doc = nlp(query)

    # 1️⃣ Try spaCy NER
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geo-Political Entity
            return ent.text.title()
    
    # 2️⃣ Fallback: find first proper noun or token after weather keyword
    tokens = query.split()
    weather_keywords = ['forecast', 'weather', 'temperature', 'hot', 'cold', 'warm', 'cool']
    for i, word in enumerate(tokens):
        if word.lower() in weather_keywords:
            # look ahead for first non-filler word
            for j in range(i+1, len(tokens)):
                if tokens[j].lower() not in filler_words:
                    return tokens[j].title()
    
    return None

# --- PROCESS TEMPERATURE QUERY ---
def process_temperature_query(query, lat=None, lon=None, city_name=None):
    """
    Processes user queries for current weather or forecast, with sentiment fallback.
    """
    tokens = nltk.word_tokenize(query.lower())
    temp_keywords = ['weather','temperature', 'hot', 'cold', 'warm', 'cool']
    forecast_keywords = ['forecast', 'prediction', 'future']

    # Ensure we have a city name
    if not city_name:
        city_name = extract_city(query)

    # Weather-related queries
    if any(k in tokens for k in temp_keywords + forecast_keywords):
        if any(k in tokens for k in forecast_keywords):
            forecast, location = get_forecast(lat, lon, city_name)
            if forecast and location:
                forecast_with_recs = {}
                for day, items in forecast.items():
                    forecast_with_recs[day] = []
                    for item in items:
                        item['recommendation'] = generate_recommendation(item['description'])
                        forecast_with_recs[day].append(item)
                return {"type": "forecast", "location": location, "forecast": forecast_with_recs}
            print(f"Forecast API failed for city: {city_name}")
            return {"error": f"Could not retrieve forecast for '{city_name}'."}
        else:
            current_weather = get_current_temperature(lat, lon, city_name)
            if current_weather:
                current_weather['recommendation'] = generate_recommendation(current_weather['description'])
                return {"type": "current", "weather": current_weather}
            print(f"Current weather API failed for city: {city_name}")
            return {"error": f"Could not retrieve current weather for '{city_name}'."}

    # Non-weather queries -> sentiment analysis fallback
    sentiment = sentiment_analyzer(query)[0]
    if sentiment['label'] == 'POSITIVE':
        return {"message": "Hello! Ask me about the weather 🌤️."}
    return {"message": "Oops! Please ask about weather-related queries."}


# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    lat = data.get('lat')
    lon = data.get('lon')
    city_name = data.get('city_name')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = process_temperature_query(user_message, lat, lon, city_name)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
