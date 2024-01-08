import requests #pip install requests
import json #
import datetime
import win32com.client #pip install pywin32


def get_weather_data(city):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    url = f"https://api.weatherapi.com/v1/current.json?key=9b3c742e6b5c436ea9a124126232509&q={city}"
    

    req = requests.get(url)
    load = json.loads(req.text)
    temp = load["current"]["temp_c"]
    print(f"The current weather of {city} is {temp} degree")
    speaker.Speak(f"The current weather of {city} is {temp} degree")

    if req.status_code == 200:
        data = json.loads(req.text)
        return data
    else:
        print(f"Error: {req.status_code}")
        return None


def save_weather_data(data):
    current_time = datetime.datetime.now()
    filename = f"weather_data_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.json"

    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_data = get_weather_data(city)

    if weather_data is not None:
        save_weather_data(weather_data)
        print("Weather data saved successfully.")
    else:
        print("Error retrieving weather data.")
