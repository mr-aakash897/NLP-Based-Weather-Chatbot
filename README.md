<b><u># NLP-Based-Weather-Chatbot </u></b>

A simple **NLP-powered chatbot** built with **Flask + OpenWeatherMap API** that provides **current weather** and **5-day forecast** for cities worldwide.  
The chatbot can understand natural language queries like:

- *"Delhi weather"*  
- *"Current temperature in Mumbai"*  
- *"Tokyo forecast for next week"*  

---

<u>## 🚀 Features </u>
- 🌍 Get **current weather** for any city.  
- 📅 Get **5-day weather forecast**.  
- 💬 Chat-like interface with bot responses.  
- 🧠 **NLP support** using spaCy for entity recognition.  
- 🎨 Simple, clean, and responsive chat UI.  
- ☁️ Weather data from **OpenWeatherMap API**.  

---

<u>## 🛠️ Tech Stack </u>
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **NLP:** spaCy, NLTK  
- **API:** OpenWeatherMap  

---

<u>## 📂 Project Structure </u>
WeatherChatbot/
│── app.py # Flask backend
│── requirements.txt # Dependencies
│── .env # API key storage
│── templates/
│ └── index.html # Chat UI


---

<u>## ⚙️ Installation & Setup </u>

### 1️⃣ Clone the repository
.bash
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

---

<u>## 📋 Example Queries : </u>
<ol><li></li>1.Here are some queries you can try directly: </li>
<li>2.Delhi weather </li>
<li>3.Mumbai temperature </li>
<li>4.Japan weather </li>
<li>5.China temperature </li>
<li>6. Russia weather </li>
<li>7. New York weather </li>
<li>8. London temperature </li>
<li>10. Tokyo weather </li>
<li>11. Paris temperature </li>
<li>12. Sydney weather </li>
<li>13. Dubai temperature </li>
<li>14. Toronto weather </li>
<li>15. Singapore temperature </li>
<li>16. Berlin weather </li></ol>

---

<u>##🚧 Known Issues : </u>
Some queries like "weather now" may fail due to NLP misinterpretation.
Requires valid city names for best results.

---

<u>##✨ Future Improvements : </u>
✅ Support for voice input.
✅ Add multiple day forecasts.
✅ Improve NLP accuracy with custom entity recognition.
✅ Dark mode UI.

---

<u>##🤝 Contributing : </u>
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.
