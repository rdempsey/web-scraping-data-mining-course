#!/usr/bin/env python
# encoding: utf-8
"""
tweepy_rest_api.py
Created by Robert Dempsey on 02/02/2016.

Example script showing how to use the Tweepy Python library to interact
with the Twitter streaming API

Tweepy docs: http://tweepy.readthedocs.org/en/v3.5.0/
Twitter API docs: https://dev.twitter.com/streaming/overview

"""

import configparser
import tweepy

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


def main():
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
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    # Use a filter to stream all tweets containing 'Trump'
    # Use async to run the stream on a new thread
    myStream.filter(track=['trump'], async=True)


if __name__ == '__main__':
    main()