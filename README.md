<h2><b><u># NLP-Based-Weather-Chatbot </u></b></h2>

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

<u>## 📂 Project Structure </u><br>
NLP-Based-Weather-Chatbot/<br>
│── app.py # Flask backend<br>
│── requirements.txt # Dependencies<br>
│── .env # API key storage<br>
│── templates/<br>
│ └── index.html # Chat UI<br>


---

<u>## ⚙️ Installation & Setup </u>

### 1️⃣ Clone the repository
.bash<br>
git clone https://github.com/mr-aakash897/NLP-Based-Weather-Chatbot.git<br>
cd NLP-Based-Weather-Chatbot<br>

### 2️⃣ Create a virtual environment
python -m venv venvnlp<br>
venvnlp\Scripts\activate    # On Windows<br>
source venvnlp/bin/activate # On Mac/Linux<br>

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your OpenWeatherMap API Key
Create a .env file in the project root and add:<br>
OPENWEATHER_API_KEY=your_api_key_here     (You can get a free API key from 👉 OpenWeatherMap.)<br>

### 5️⃣ Run the project
python app.py<br>
(The app will start at 👉 http://127.0.0.1:5000)

---

<u>## 📋 Example Queries : </u><br>
<ol><li>Here are some queries you can try directly: </li>
<li>Delhi weather </li>
<li>Mumbai temperature </li>
<li>Japan weather </li>
<li>China temperature </li>
<li> Russia weather </li>
<li> New York weather </li>
<li> London temperature </li>
<li> Tokyo weather </li>
<li> Paris temperature </li>
<li> Sydney weather </li>
<li> Dubai temperature </li>
<li> Toronto weather </li>
<li> Singapore temperature </li>
<li> Berlin weather </li></ol>

---

<u>##🚧 Known Issues : </u><br>
<li>Some queries like "weather now" may fail due to NLP misinterpretation.</li>
<li>Requires valid city names for best results.</li>

---

<u>##✨ Future Improvements : </u><br>
<li>✅ Support for voice input.</li>
<li>✅ Add multiple day forecasts.</li>
<li>✅ Improve NLP accuracy with custom entity recognition.</li>
<li>✅ Dark mode UI.</li>

---

<u>##🤝 Contributing : </u>
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.
