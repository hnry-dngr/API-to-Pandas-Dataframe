# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 01:18:37 2024

@author: HP
"""

import requests
import pandas as pd

url = "https://api.nasa.gov/planetary/apod"
url1 = "https://api.nasa.gov/planetary/apod?api_key=GqNeecIb7e9gWOHJGcZ60JrEjiUHhYxnruszqNjk"
# https://apod.nasa.gov/apod/astropix.html
scraper = requests.get(url1)
response = scraper.json()


querystring = {"fragment":"true","notfound":"floor","json":"true"}

headers = {
	"X-RapidAPI-Key": "GqNeecIb7e9gWOHJGcZ60JrEjiUHhYxnruszqNjk",
	"X-RapidAPI-Host": "api.nasa.gov"
}

dataset = pd.json_normalize(response)

explanation = dataset.get("explanation", "Explanation not available")


# Asteroid ID
# Asteroid name
# The Minimal estimated diameter in Kilometre
# Absolute_magnitude
# Relative_velocity(km/s)


# data, columns=["copyright", "date", "explanation", "hdurl", "media_type", "service_version", "title", "url"
