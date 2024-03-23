This Python script demonstrates speech recognition and automated tasks using various APIs and libraries. It allows users to perform two main tasks: sending emails and retrieving weather forecasts, all through voice commands.

Features:
Speech Recognition: Utilizes the speech_recognition library to convert spoken words into text.
Intent Recognition: Recognizes the user's intent based on the spoken command using natural language processing techniques.
Email Sending: Sends emails via Gmail SMTP server using the smtplib library.
Weather Forecast: Retrieves weather forecast data from the OpenWeatherMap API based on the user's location.
Text-to-Speech: Converts text messages into speech using the pyttsx3 library.

Prerequisites:
Python 3.x installed on your system
Required Python libraries: speech_recognition, nltk, pyttsx3, smtplib, requests
Active internet connection

Usage:
Install the required Python libraries using pip:
pip install speech_recognition nltk pyttsx3 requests
Configure Gmail credentials:
Set the GMAIL_USER and GMAIL_PASSWORD variables with your Gmail email address and password.
Run the script:
python speech_recognition_tasks.py
Speak a command when prompted, such as "Send an email" or "What's the weather forecast?"

Note:
Ensure that your microphone is properly configured and accessible by the script.
Replace the email recipients, weather location, and OpenWeatherMap API key with your own values as needed.
The script may require additional setup or permissions on your system to access the microphone and send emails.

Disclaimer:
This script is provided for educational purposes only. Use it responsibly and ensure compliance with all applicable laws and regulations, especially regarding email communications and data privacy.

Author:
AMRITANGSHU DASKAR

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments:
Special thanks to the developers of the libraries and APIs used in this project.
