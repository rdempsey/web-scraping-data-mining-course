#!/usr/bin/env python
# encoding: utf-8

"""
Created by Robert Dempsey on 02/03/2016.

Example script showing how to use the python-forecastio Python library
to interact with the Forecast.io REST API.

python-forecastio docs: https://github.com/ZeevG/python-forecast.io
Forecast.io API docs: https://github.com/ZeevG/python-forecast.io

"""

import configparser

import forecastio


def main():
    """Get the current forecast from Forecast.io."""
    # Read the config file and get the goodies
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    # Set all of the variables we need for Forecast.io
    api_key = config['Forecastio']['api_key']
    lat = config['Forecastio']['default_lat']
    lon = config['Forecastio']['default_lon']

    # Authenticate with Forecast.io and get the current forecast
    try:
        f = forecastio.load_forecast(api_key, lat, lon)
        forecast = f.daily()
        # Get the forecast summary
        f_summary = forecast.data[0].summary[:-1].lower()
        # Get the rest of the temps for the day
        f_min_temp = int(round(forecast.data[0].temperatureMin))
        f_max_temp = int(round(forecast.data[0].temperatureMax))
        # Create the forecast
        print("It is going to be {} with temperatures between {} and {}"
              " degrees".format(f_summary, f_min_temp, f_max_temp))
    except:
        print("nable to retrieve the current weather forecast")


if __name__ == '__main__':
    main()
