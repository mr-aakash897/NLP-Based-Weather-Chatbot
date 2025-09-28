<b># NLP-Based-Weather-Chatbot </b>

A simple **NLP-powered chatbot** built with **Flask + OpenWeatherMap API** that provides **current weather** and **5-day forecast** for cities worldwide.  
The chatbot can understand natural language queries like:

- *"Delhi weather"*  
- *"Current temperature in Mumbai"*  
- *"Tokyo forecast for next week"*  

---

## 🚀 Features
- 🌍 Get **current weather** for any city.  
- 📅 Get **5-day weather forecast**.  
- 💬 Chat-like interface with bot responses.  
- 🧠 **NLP support** using spaCy for entity recognition.  
- 🎨 Simple, clean, and responsive chat UI.  
- ☁️ Weather data from **OpenWeatherMap API**.  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **NLP:** spaCy, NLTK  
- **API:** OpenWeatherMap  

---

## 📂 Project Structure
WeatherChatbot/
│── app.py # Flask backend
│── requirements.txt # Dependencies
│── .env # API key storage
│── templates/
│ └── index.html # Chat UI


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mr-aakash897/NLP-Based-Weather-Chatbot.git
cd NLP-Based-Weather-Chatbot

### 2️⃣ Create a virtual environment
python -m venv venvnlp
venvnlp\Scripts\activate    # On Windows
source venvnlp/bin/activate # On Mac/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your OpenWeatherMap API Key
Create a .env file in the project root and add:
OPENWEATHER_API_KEY=your_api_key_here     (You can get a free API key from 👉 OpenWeatherMap.)

### 5️⃣ Run the project
python app.py
(The app will start at 👉 http://127.0.0.1:5000)

### 📋 Example Queries
1.Here are some queries you can try directly:
2.Delhi weather
3.Mumbai temperature
4.Japan weather
5.China temperature
6. Russia weather
7. New York weather
8. London temperature
10. Tokyo weather
11. Paris temperature
12. Sydney weather
13. Dubai temperature
14. Toronto weather
15. Singapore temperature
16. Berlin weather

🚧 Known Issues:
Some queries like "weather now" may fail due to NLP misinterpretation.
Requires valid city names for best results.

✨ Future Improvements: 
✅ Support for voice input.
✅ Add multiple day forecasts.
✅ Improve NLP accuracy with custom entity recognition.
✅ Dark mode UI.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.