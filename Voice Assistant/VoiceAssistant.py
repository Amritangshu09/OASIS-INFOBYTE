import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
import pyttsx3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize NLTK
nltk.download('punkt')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Gmail credentials
GMAIL_USER = 'abc@gmail.com'
GMAIL_PASSWORD = 'abc123'

# Function to perform intent recognition
def recognize_intent(text):
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())

    # Example intent recognition logic
    if 'email' in tokens and 'send' in tokens:
        return 'send_email'
    elif 'weather' in tokens and 'forecast' in tokens:
        return 'weather_forecast'
    else:
        return 'unknown'

# Function to send email using Gmail API
def send_email(receiver_email, subject, body):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        message = MIMEMultipart()
        message['From'] = GMAIL_USER
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(GMAIL_USER, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

# Function to get weather forecast using Weather Forecast API
def get_weather_forecast():
    api_key = 'YOUR_API_KEY'
    lat=#your latitude
    lon=#your longitude
    city = 'New York'  # Replace 'New York' with your desired city
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    # Parse the weather forecast data and return
    return data
# Capture audio from the microphone
def capture_audio():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    return audio

# Speech recognition and intent recognition
def process_audio():
    audio = capture_audio()

    # Recognize speech using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        intent = recognize_intent(text)
        print("Intent: " + intent)

        if intent == 'send_email':
            send_email('xyz@gmail.com', 'Test email system', 'This is a test email made using Python and API ')
            speak("Email sent successfully!")
        elif intent == 'weather_forecast':
            # Replace lat, lon, and api_key with your values
            lat = #your latitude
            lon = #your longitude
            api_key = 'YOUR_API _KEY'
            
            weather_data = get_weather_forecast()
            print("Weather Data:\n", weather_data)  # Debugging: Print weather data
            
            # Extract relevant weather information
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']

            # Convert temperature from Kelvin to Celsius
            temperature_celsius = temperature - 273.15

            # Format weather information
            weather_message = f"The temperature is {temperature_celsius:.2f} degrees Celsius with {description}."

            # Speak weather forecast
            speak(weather_message)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    process_audio()
