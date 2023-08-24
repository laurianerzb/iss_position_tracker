# ISS Position Tracker

![App Screenshot]()

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Author](#author)

## Description
This program tracks the International Space Station (ISS) and notifies you if 
it's close to your location and if it's nighttime. It uses the ISS API to determine 
the ISS's position and the Sunrise-Sunset API to determine the sunrise and sunset 
times for your location.


## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- `smtplib` library (standard library)
- An email account for sending notifications
- ISS position (`MY_LAT`, `MY_LONG`) and your email credentials (`MY_EMAIL`, `PASSWORD`) configured in the script

## Features

- Retrieves the ISS's current position using the ISS API.
- Determines if the ISS is within +5 or -5 degrees of your specified latitude and longitude.
- Retrieves sunrise and sunset times for your location using the Sunrise-Sunset API.
- Determines if it's currently nighttime based on the retrieved times.
- Sends an email notification to your specified email address if the ISS is close and it's nighttime.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/laurianerzb/iss_position_tracker.git
2. Navigate to the project directory:
   ```bash 
   cd iss_position_tracker
3. Replace "your@email.com" with your Gmail email address in the MY_EMAIL variable.
4. Provide your Gmail account password by replacing the empty string "" with your 
actual password provided by the two-factor authentication in the PASSWORD variable. 
Note: Storing passwords directly in your script is not recommended for security reasons. Consider using environment variables or a more secure method to store credentials.
5. Run the program
   ```bash
   python iss_poosition_tracker.py

## Author
- [laurianerzb](https://github.com/laurianerzb)
