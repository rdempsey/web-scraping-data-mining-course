#!/usr/bin/env python
# encoding: utf-8

"""
Created by Robert Dempsey on 02/02/2016.

Example script showing how to use the Tweepy Python library to interact
with the Twitter REST API, using available models

Tweepy docs: http://tweepy.readthedocs.org/en/v3.5.0/
Twitter API docs: https://dev.twitter.com/rest/public

"""

import configparser

import tweepy


def main():
    """Look up a user and get the top 20 friends and their statuses."""
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
    user = api.get_user('DistrictDataLab')

    # Print out various information about the user
    print("Screen name: {}".format(user.screen_name))
    print("Follower count: {}\n".format(user.followers_count))
    print("User Friend List (20)\n")
    for friend in user.friends():
        print("Screen name: {}".format(friend.screen_name))
        print("Follower count: {}".format(friend.followers_count))
        print("Latest status: {}\n".format(friend.status.text))


if __name__ == '__main__':
    main()
