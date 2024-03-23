import tkinter as tk
import requests

def fetch_weather_data(location):
    api_key = '7c7d1a4de00541f11af07f6aec5e1a19'
    #lat=22.5726
    #lon=88.3639
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data
    # Connect to a weather API and fetch weather data based on the location
    #api_key = 'YOUR_API_KEY'
    #url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    #response = requests.get(url)
    #data = response.json()
    #return data

def display_weather_data(data):
    # Extract relevant weather information from the JSON data
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    # Display weather data in the GUI
    weather_label.config(text=f'Temperature: {temperature}°C\nWeather: {weather_description}\nWind Speed: {wind_speed} m/s')

def get_weather():
    location = location_entry.get()
    weather_data = fetch_weather_data(location)
    display_weather_data(weather_data)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
location_label = tk.Label(root, text="Enter Location:")
root.geometry("200x200")
location_label.pack()

location_entry = tk.Entry(root)
location_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

# Run the application
root.mainloop()
