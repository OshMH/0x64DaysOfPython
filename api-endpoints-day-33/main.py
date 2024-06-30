import requests
import datetime
from icecream import ic

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# logitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (logitude, latitude)
# print(iss_position)



"""# Reponse codes:
# 1xx means hold on, something is happening
# 2xx means everything went well, here is what you asked for
# 3xx means go away you dont have permissions for this
# 4xx means you screwed up
# 5xx means the server screwed up
"""
MY_LAT = -36.884460
MY_LNG = 174.682641
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data= response.json()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
time_now = datetime.datetime.now()
ic(f"sunset: {sunset} sunrise: {sunrise} time now: {time_now} ")
