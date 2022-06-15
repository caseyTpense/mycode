#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    epoch_time= resp["timestamp"]
    date_time= datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-5d %H:%M:%S')

    lat=  resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"]

    coords_tuple= (lat, lon)
    result = rg.search(coords_tuple)
    city = [d['admin2'] for d in result]
    cc = [d['cc'] for d in result]
    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (lat, lon)

    

    print("CURRENT LOCATION OF THE ISS:\n","Timestamp:", date_time, "\n", resp["iss_position"]["longitude"], "\n", resp["iss_position"]["latitude"], '\nCity/State:', city, cc)
if __name__ == "__main__":
    main()
