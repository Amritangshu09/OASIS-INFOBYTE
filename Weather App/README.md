**Weather App**

This Python script implements a simple weather application using the Tkinter library for creating a graphical user interface (GUI) and the OpenWeatherMap API for fetching weather data. Users can input a location (city name) and click the "Get Weather" button to retrieve the current weather information for that location.

### Features:
1. **Graphical User Interface (GUI):** Utilizes Tkinter, a standard GUI toolkit for Python, to create an interactive interface for the weather application.
2. **Weather Data Retrieval:** Fetches current weather data from the OpenWeatherMap API based on the user-provided location.
3. **Display Weather Information:** Displays temperature, weather description, and wind speed for the specified location.
4. **Input Validation:** Validates user input to ensure that a location is provided before attempting to fetch weather data.
5. **Units Conversion:** Retrieves weather data in metric units (temperature in Celsius, wind speed in meters per second) for easy interpretation.

### Prerequisites:
- Python 3.x installed on your system
- Tkinter library (usually comes pre-installed with Python)
- Requests library (`pip install requests`)

### Usage:
1. Ensure that you have Python installed on your system.
2. Install the Requests library if not already installed:
   ```
   pip install requests
   ```
3. Run the script:
   ```
   python weather_app.py
   ```
4. Enter the desired location (city name) into the input field.
5. Click the "Get Weather" button to fetch and display the current weather information for the specified location.
6. The temperature, weather description, and wind speed will be displayed below the input field.

### Note:
- This weather application provides basic functionality for retrieving and displaying current weather data. Additional features such as forecasting, graphical representations, and location suggestions can be implemented for enhanced user experience.
- Ensure that you have a valid API key for accessing the OpenWeatherMap API. You can sign up for a free account on the OpenWeatherMap website to obtain an API key.

### Author:
- AMRITANGSHU DASKAR

### License:
- This project is licensed under the MIT License 

### Acknowledgments:
- Special thanks to the developers of Tkinter and the OpenWeatherMap API for providing the tools and resources to create this weather application.
