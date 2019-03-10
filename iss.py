import requests
import json
from datetime import datetime

def get_iss_location():
    endpoint = 'http://api.open-notify.org/iss-now.json'

    # Return in json format {"iss_position": {"latitude": "-49.4665", "longitude": "-51.0737"}, "message": "success", "timestamp": 1552249236}

def get_iss_pass_time(lat, long):
    endpoint = 'http://api.open-notify.org/iss-pass.json'

    # Return in following format 2019-03-10 23:56:31
def get_iss_pass_time_from_postcode(postcode):
    endpoint = f'http://api.postcodes.io/postcodes/{postcode}'

    # Return in following format 2019-03-10 23:56:31
