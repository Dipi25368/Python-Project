import requests
API_KEY = "79a82a0a937d8a078dd0d940bd8b92a1"
CITY = input("Enter city: ")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
        data = response.json()
            
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        
        print(f"City: {CITY}")
        print(f"Temperature: {temperature}C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
else:
        print("Error fetching weather data")