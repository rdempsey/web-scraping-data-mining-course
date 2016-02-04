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
    """Get the current weather from Forecast.io."""
    # Read the config file and get the goodies
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    # Set all of the variables we need for Forecast.io
    api_key = config['Forecastio']['api_key']
    lat = config['Forecastio']['default_lat']
    lon = config['Forecastio']['default_lon']

    # Authenticate with Forecast.io and get the current weather report
    try:
        forecast = forecastio.load_forecast(api_key, lat, lon)
        c = forecast.currently()
        c_temp = int(round(c.temperature))
        c_summary = c.summary.lower()
        c_precip = int(round(c.precipProbability * 100))
        print("It is currently {} degrees and {} with a {} percent chance of"
              " precipitation.".format(c_temp, c_summary, c_precip))
    except:
        print("Unable to retrieve the current weather report")

if __name__ == '__main__':
    main()
