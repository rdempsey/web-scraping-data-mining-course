#!/usr/bin/env python
# encoding: utf-8

"""
Created by Robert Dempsey on 02/02/2016.

Example script showing how to use the Tweepy Python library to interact
with the Twitter streaming API and save the tweets to a SQLite database.

Tweepy docs: http://tweepy.readthedocs.org/en/v3.5.0/
Twitter API docs: https://dev.twitter.com/streaming/overview

"""

import configparser

import sqlite3

from datetime import datetime

import tweepy


class MyStreamListener(tweepy.StreamListener):
    """Overrides tweepy.StreamListener to add logic to on_status."""

    conn = ""
    cursor = ""

    def __init__(self, api):
        """Initialize the class with the api."""
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def save_status(self, status):
        """Save the status to the database."""
        # Connect to the SQLite database
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        db = config['Twitter']['twitter_db']
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        try:
            created_at = str(datetime.now())
            cursor.execute('''INSERT INTO tweets (tweet, created_at)
                              VALUES(?,?)''', (status, created_at))
            conn.commit()
        except sqlite3.OperationalError as err:
            print("SQL Insert Error: {}".format(err))

    def on_status(self, status):
        """Print out the text of the tweet and save it to the database."""
        print(status.text)
        self.save_status(status.text)

    def on_error(self, status_code):
        """
        Error handling.

        If the API returns a status code of 420 return False and
        disconnect the data stream.
        """
        if status_code == 420:
            return False


def main():
    """Get the 10 latest tweets from your timeline."""
    # Read the config file and get the goodies
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    # Set all of the variables we need for Twitter
    consumer_key = config['Twitter']['consumer_key']
    consumer_secret = config['Twitter']['consumer_secret']
    access_token = config['Twitter']['access_token']
    access_token_secret = config['Twitter']['access_token_secret']

    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create an API object
    api = tweepy.API(auth)

    # Create a stream
    my_listener = MyStreamListener(api)
    streamer = tweepy.Stream(auth=api.auth, listener=my_listener)

    # Use a filter to stream all tweets containing 'Trump'
    # Use async to run the stream on a new thread
    streamer.filter(track=['trump'], async=True)


if __name__ == '__main__':
    main()
