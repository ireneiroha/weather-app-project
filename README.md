🌦️ Weather App
A simple Django web application that allows users to check the current weather for any city using real-time weather data.
Built with Django, Python, and a weather API (e.g., OpenWeatherMap).

📋 Features
Search for any city and get current weather details

Displays temperature, humidity, and weather conditions

Beautiful and responsive frontend (optional: add Bootstrap)

Error handling for invalid city names

Clean and simple design

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS (optional: Bootstrap)

API: OpenWeatherMap

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/ireneiroha/weather-app-project
cd weather-app
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
3. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
(Create requirements.txt using pip freeze > requirements.txt)

4. Set up environment variables
Create a .env file in the root directory and add your API key:

bash
Copy
Edit
WEATHER_API_KEY=your_openweathermap_api_key_here
(Use django-environ to manage it securely.)

5. Run database migrations
bash
Copy
Edit
python manage.py migrate
6. Run the development server
bash
Copy
Edit
python manage.py runserver
Then open http://127.0.0.1:8000/ in your browser!

🧠 Project Structure
cpp
Copy
Edit
weatherProject/
├── weatherApp/
│   ├── migrations/
│   ├── templates/
│   │   └── weatherApp/
│   │       └── index.html
│   ├── static/
│   │   └── weatherApp/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── weatherProject/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
└── README.md
🎯 To-Do / Improvements
Add forecast for the next few days

Show local time of the city

Improve UI with animations

Deploy to Heroku, Vercel, or Railway

💬 Acknowledgements
Django Documentation

OpenWeatherMap API

Bootstrap

📜 License
This project is open-source and available under the MIT License.


