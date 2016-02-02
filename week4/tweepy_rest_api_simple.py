#!/usr/bin/env python
# encoding: utf-8

"""
Created by Robert Dempsey on 02/02/2016.

Example script showing how to use the Tweepy Python library to interact
with the Twitter REST API

Tweepy docs: http://tweepy.readthedocs.org/en/v3.5.0/
Twitter API docs: https://dev.twitter.com/rest/public

"""

import configparser
import tweepy


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

    # Create an API object to use
    api = tweepy.API(auth)

    # Get the latest tweets
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text + "\n")


if __name__ == '__main__':
    main()
