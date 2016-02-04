#!/usr/bin/env python
# encoding: utf-8

"""
Created by Robert Dempsey on 02/04/2016.

Example script showing how to use the python-forecastio Python library
to interact with the Forecast.io REST API and save the forecast data
to a SQLite database.

python-forecastio docs: https://github.com/ZeevG/python-forecast.io
Forecast.io API docs: https://github.com/ZeevG/python-forecast.io

"""

import configparser

import sqlite3

# from datetime import datetime

import forecastio


def save_forecast(lat, lon, forecast):
    """Save a forecast to the database."""
    # Connect to the SQLite database
    config = configparser.ConfigParser()
    config.read('../config/config.ini')
    db = config['Forecastio']['forecast_db']
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Get the forecast for the day
    f = forecast.daily()
    # Get all of the forecast information
    utime = f.data[0].utime
    sunset_time = f.data[0].sunsetTime
    sunrise_time = f.data[0].sunriseTime
    wind_speed = f.data[0].windSpeed
    temperature_max_time = f.data[0].temperatureMaxTime
    ozone = f.data[0].ozone
    temperature_max = f.data[0].temperatureMax
    pressure = f.data[0].pressure
    humidity = f.data[0].humidity
    moon_phase = f.data[0].moonPhase
    precip_intensity_max = f.data[0].precipIntensityMax
    cloud_cover = f.data[0].cloudCover
    icon = f.data[0].icon
    precip_probability = f.data[0].precipProbability
    temperature_min_time = f.data[0].temperatureMinTime
    temperature_min = f.data[0].temperatureMin
    precip_intensity_max_time = f.data[0].precipIntensityMaxTime
    visibility = f.data[0].visibility
    precip_type = f.data[0].precipType
    dew_point = f.data[0].dewPoint
    summary = f.data[0].summary
    apparent_temperature_max_time = f.data[0].apparentTemperatureMaxTime
    apparent_temperature_max = f.data[0].apparentTemperatureMax
    wind_bearing = f.data[0].windBearing
    apparent_temperature_min_time = f.data[0].apparentTemperatureMinTime
    apparent_temperature_min = f.data[0].apparentTemperatureMin
    precip_intensity = f.data[0].precipIntensity

    try:
        # created_at = str(datetime.now())
        cursor.execute('''INSERT INTO forecasts (utime, sunset_time, wind_speed,
                        temperature_max_time,
                        ozone, temperature_max, apparent_temperature_min_time,
                        pressure, humidity, moon_phase, precip_intensity_max,
                        cloud_cover, icon, precip_probability,
                        temperature_min_time, temperature_min,
                        precip_intensity_max_time, visibility,
                        sunrise_time, precip_type, dew_point, summary,
                        apparent_temperature_max_time,
                        apparent_temperature_max, wind_bearing,
                        apparent_temperature_min, precip_intensity)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                               ?,?,?)''',
                       (utime, sunset_time, wind_speed, temperature_max_time,
                        ozone, temperature_max, apparent_temperature_min_time,
                        pressure, humidity, moon_phase, precip_intensity_max,
                        cloud_cover, icon, precip_probability,
                        temperature_min_time, temperature_min,
                        precip_intensity_max_time, visibility,
                        sunrise_time, precip_type, dew_point, summary,
                        apparent_temperature_max_time,
                        apparent_temperature_max, wind_bearing,
                        apparent_temperature_min, precip_intensity))
        conn.commit()
        print("Forecast saved")
    except sqlite3.OperationalError as err:
        print("SQL Insert Error: {}".format(err))


def main():
    """Get weather data from Forecast.io and save it to a database."""
    # Read the config file and get the goodies
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    # Set all of the variables we need for Forecast.io
    api_key = config['Forecastio']['api_key']
    lat = config['Forecastio']['default_lat']
    lon = config['Forecastio']['default_lon']

    # Authenticate with Forecast.io, get the current forecast and
    # save to the database
    forecast = forecastio.load_forecast(api_key, lat, lon)
    save_forecast(lat, lon, forecast)


if __name__ == '__main__':
    main()
