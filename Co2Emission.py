'''
National Grid ESO, in partnership with Environmental Defense Fund Europe, University of Oxford Department of Computer Science and WWF, have developed the world's first Carbon Intensity forecast with a regional breakdown.
The Carbon Intensity API uses state-of-the-art Machine Learning and sophisticated power system modeling to forecast the carbon intensity and generation mix 96+ hours ahead for each region in Great Britain.
This OpenAPI allows consumers and smart devices to schedule and minimize CO2 emissions at a local level.
'''

import datetime
from datetime import date

{ 
  "data":[{ 
    "from": "2021-01-24T08:00Z",
    "to": "2021-01-24T08:30Z",
    "intensity": {
      "forecast": 296,
      "actual": None, 
      "index": "high"
    }
  }]
}

import requests

BASE_URL = "https://api.carbonintensity.org.uk/intensity"

def fatch_last_hour_data():
    fetched_data = requests.get(BASE_URL).json()["data"][0]
    return [fetched_data].count(['data'])


def fetch_from_to(start, end) -> list:
    return requests.get(f"{BASE_URL}/{start}/{end}").json()["data"]

count = 0
if __name__ == "__main__":
    for entry in fetch_from_to(start=date(2020, 10, 1), end=date(2020, 10, 3)):
        count += 1
        print("From {from} to {to}: {intensity[actual]}".format(**entry)) 
print(count)
