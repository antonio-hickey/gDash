"""
gDash
By: Antonio Hickey

Micro Miner is for mining data on local event's for me this mean's the United States

The bot is reading tweet's from @IntelPointAlert on Twitter an informant reporting major
and active incidents as they occur in the US. https://twitter.com/IntelPointAlert

1. Read's recent tweet's
    - Look's for urgent event's
        - Find's what state it's taking place
            - set lat & lon for x state
        - Summerize event
        - Store data
2. Export collected data to csv for use in app
    - filename: "local_events.csv"
"""


# Import modules
import csv
import datetime as dt
import os

import tweepy

# Current Event's
today = dt.datetime.today().strftime('%m/%d/%Y')

# CHANGE WITH YOUR TWITTER API KEYS | it's free apply @ (https://developer.twitter.com/en)
auth = tweepy.OAuthHandler('*YOUR CONSUMER KEY*', '*YOUR SECRET CONSUMER KEY*')
auth.set_access_token('*YOUR ACCESS TOKEN*', '*YOUR SECRET ACCESS TOKEN*')
api = tweepy.API(auth)


# Setting our user source (Defualt: https://twitter.com/IntelPointAlert)
tweets = api.user_timeline('IntelPointAlert')


# null outputs to store collected data
lat = []
lon = []
descrip = []
link = []


# Looping through each tweet
for tweet in tweets:
    if '#URGENT' in tweet.text:
        # Alabama
        if '#AL' in tweet.text:
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Alaska
        if '#AK' in tweet.text:
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # American Samoa
        if '#AS' in tweet.text:
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Arizona
        if '#AZ' in tweet.text:
            lat.append(34.446561)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Arkansas
        if '#AR' in tweet.text:
            lat.append(34.795930)
            lon.append(-92.362050)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # California
        if '#CA' in tweet.text:
            lat.append(36.270146)
            lon.append(-119.650223)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Colorado
        if '#CO' in tweet.text:
            lat.append(39.026163)
            lon.append(105.781686)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Connecticut
        if '#CT' in tweet.text:
            lat.append(41.703206)
            lon.append(-72.646089)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Delaware
        if '#DE' in tweet.text:
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # District of Columbia
        if '#DC' in tweet.text:
            lat.append(38.885778)
            lon.append(-77.013282)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Florida
        if '#FL' in tweet.text:
            lat.append(27.451115)
            lon.append(-81.255174)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Georgia
        if '#GA' in tweet.text:
            lat.append(32.876795)
            lon.append(-83.483814)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Guam
        if '#GU' in tweet.text:
            lat.append(13.410410)
            lon.append(144.733354)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Hawaii
        if '#HI' in tweet.text:
            lat.append(20.756709)
            lon.append(-156.300641)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Idaho
        if '#ID' in tweet.text:
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Illinois
        if '#IL' in tweet.text:
            lat.append(40.385585)
            lon.append(-88.997220)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Indiana
        if '#IN' in tweet.text:
            lat.append(39.938679)
            lon.append(-86.071216)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Iowa
        if '#IA' in tweet.text:
            lat.append(41.857857)
            lon.append(-93.268631)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Kansas
        if '#KS' in tweet.text:
            lat.append(38.360213)
            lon.append(-98.424674)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Kentucky
        if '#KY' in tweet.text:
            lat.append(37.557950)
            lon.append(-84.475312)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Louisiana
        if '#LA' in tweet.text:
            lat.append(30.632183)
            lon.append(-92.039792)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Maine
        if '#ME' in tweet.text:
            lat.append(44.879165)
            lon.append(-69.156696)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Maryland
        if '#MD' in tweet.text:
            lat.append(39.356961)
            lon.append(-76.9165257)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Massachusetts
        if '#MA' in tweet.text:
            lat.append(42.270030)
            lon.append(-71.699885)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Michigan
        if '#MI' in tweet.text:
            lat.append(42.866290)
            lon.append(-84.514843)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Minnesota
        if '#MN' in tweet.text:
            lat.append(45.726258)
            lon.append(-94.483332)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Mississippi
        if '#MS' in tweet.text:
            lat.append(32.829128)
            lon.append(-89.855683)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Missouri
        if '#MO' in tweet.text:
            lat.append(38.735015)
            lon.append(-92.480738)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Montana
        if '#MT' in tweet.text:
            lat.append(47.197600)
            lon.append(-109.662487)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Nebraska
        if '#NE' in tweet.text:
            lat.append(41.242098)
            lon.append(-99.318614)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Nevada
        if '#NV' in tweet.text:
            lat.append(38.903271)
            lon.append(-116.426747)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # New Hampshire
        if '#NH' in tweet.text:
            lat.append(43.229182)
            lon.append(-71.576017)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # New Jersey
        if '#NJ' in tweet.text:
            lat.append(40.011891)
            lon.append(-74.505838)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # New Mexico
        if '#NM' in tweet.text:
            lat.append(34.477320)
            lon.append(-106.164719)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # New York
        if '#NY' in tweet.text:
            lat.append(40.711634)
            lon.append(-73.936331)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # North Carolina
        if '#NC' in tweet.text:
            lat.append(35.777766)
            lon.append(-78.912974)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # North Dokota
        if '#ND' in tweet.text:
            lat.append(47.120741)
            lon.append(-100.355791)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Northern Mariana Island's
        if '#MP' in tweet.text:
            lat.append(15.177288)
            lon.append(145.742024)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Ohio
        if '#OH' in tweet.text:
            lat.append(40.140730)
            lon.append(-82.799507)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Oklahoma
        if '#OK' in tweet.text:
            lat.append(35.598095)
            lon.append(-97.402951)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Oregon
        if '#OR' in tweet.text:
            lat.append(43.655112)
            lon.append(-120.709186)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Pennsylvania
        if '#PA' in tweet.text:
            lat.append(40.708446)
            lon.append(-77.797431)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Puerto Rico
        if '#PR' in tweet.text:
            lat.append(18.245539)
            lon.append(-66.476129)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Rhode Island
        if '#RI' in tweet.text:
            lat.append(41.717487)
            lon.append(-71.523872)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # South Carolina
        if '#SC' in tweet.text:
            lat.append(34.010105)
            lon.append(-80.540033)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # South Dakota
        if '#SD' in tweet.text:
            lat.append(44.418085)
            lon.append(-100.351359)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Tennessee
        if '#TN' in tweet.text:
            lat.append(35.843349)
            lon.append(-86.584571)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Texas
        if '#TX' in tweet.text:
            lat.append(31.211550)
            lon.append(-99.087012)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Utah
        if '#UT' in tweet.text:
            lat.append(39.066880)
            lon.append(-111.276458)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Vermont
        if '#VT' in tweet.text:
            lat.append(44.229969)
            lon.append(-72.741321)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Virginia
        if '#VA' in tweet.text:
            lat.append(37.519345)
            lon.append(-78.230240)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Virgin Islands
        if '#VI' in tweet.text:
            lat.append(17.731312)
            lon.append(-64.762878)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Washington
        if '#WA' in tweet.text:
            lat.append(47.094056)
            lon.append(-120.494907)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # West Virginia
        if '#WV' in tweet.text:
            lat.append(38.398489)
            lon.append(-81.000907)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Wisconsin
        if '#WI' in tweet.text:
            lat.append(44.238824)
            lon.append(-89.492394)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        # Wyoming
        if '#WY' in tweet.text:
            lat.append(43.236438)
            lon.append(-107.514572)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

# Export to csv
filename = "local_events.csv"
cols = ['Lat', 'Lon', 'Description', 'Link']
nRows = len(lat)
os.chdir(os.path.dirname(__file__))
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    for n_row in range(nRows):
        row = [lat[n_row], lon[n_row], descrip[n_row], link[n_row]]
        csvwriter.writerow(row)
