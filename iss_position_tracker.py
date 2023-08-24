import requests
from datetime import datetime
import smtplib

MY_LAT = 39.133331
MY_LONG = 117.183334
# your email
MY_EMAIL = "your@email.com"
# your password(the password provide by the  two-factor authentication)
PASSWORD = ""


def close_to_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


if close_to_iss() and is_night():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(MY_EMAIL, PASSWORD)
        server.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look up\n\nYour position is within +5 or -5 degrees "
                f"of the ISS position."
        )
