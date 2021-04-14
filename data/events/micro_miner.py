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

#-----------------------------
# Import Modules
#-----------------------------
import pandas as pd
import tweepy
import datetime as dt
import pathlib
import json
import csv
import os
#-----------------------------
# Current Event's
#-----------------------------
today = dt.datetime.today().strftime('%m/%d/%Y')
auth = tweepy.OAuthHandler('iJUY2n80SQGQMFLj4gWVQ02pd','OUGCftzYurDHlNeQkjIqrwLYlFVatvV84tsppmMKeu3e5rIzdP')
auth.set_access_token('1187682165754155010-ZwpjogKoPHAn6tKya92I53dLbPkhpK', 'C0P21qqPiOt30JMK4IWnQ22whFgsjjY41BEqUId41rP4Z')
api = tweepy.API(auth)
tweets = api.user_timeline('IntelPointAlert')

# null outputs to store collected data
lat =[]
lon = []
descrip = []
link = []

# Looping through each tweet
for tweet in tweets:

    # Look for Urgent event's
    if '#URGENT' in tweet.text:

        # Figure out what state the tweet is about
        if '#AL' in tweet.text: # Alabama
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)

        if '#AK' in tweet.text: # Alaska
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#AS' in tweet.text: # American Samoa
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#AZ' in tweet.text: # Arizona
            lat.append(34.446561)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#AR' in tweet.text: # Arkansas
            lat.append(34.795930)
            lon.append(-92.362050)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#CA' in tweet.text: # California
            lat.append(36.270146)
            lon.append(-119.650223)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#CO' in tweet.text: # Colorado
            lat.append(39.026163)
            lon.append(105.781686)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#CT' in tweet.text: # Connecticut
            lat.append(41.703206)
            lon.append(-72.646089)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#DE' in tweet.text: # Delaware
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#DC' in tweet.text: # District of Columbia
            lat.append(38.885778)
            lon.append(-77.013282)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
             
        if '#FL' in tweet.text: # Florida
            lat.append(27.451115)
            lon.append(-81.255174)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                 
        if '#GA' in tweet.text: # Georgia
            lat.append(32.876795)
            lon.append(-83.483814)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#GU' in tweet.text: # Guam
            lat.append(13.410410)
            lon.append(144.733354)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#HI' in tweet.text: # Hawaii
            lat.append(20.756709)
            lon.append(-156.300641)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#ID' in tweet.text: # Idaho
            lat.append(32.816427)
            lon.append(-86.636516)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#IL' in tweet.text: # Illinois
            lat.append(40.385585)
            lon.append(-88.997220)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
             
        if '#IN' in tweet.text: # Indiana
            lat.append(39.938679)
            lon.append(-86.071216)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#IA' in tweet.text: # Iowa
            lat.append(41.857857)
            lon.append(-93.268631)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#KS' in tweet.text: # Kansas
            lat.append(38.360213)
            lon.append(-98.424674)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#KY' in tweet.text: # Kentucky
            lat.append(37.557950)
            lon.append(-84.475312)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
             
        if '#LA' in tweet.text: # Louisiana
            lat.append(30.632183)
            lon.append(-92.039792)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                  
        if '#ME' in tweet.text: # Maine
            lat.append(44.879165)
            lon.append(-69.156696)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#MD' in tweet.text: # Maryland
            lat.append(39.356961)
            lon.append(-76.9165257)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#MA' in tweet.text: # Massachusetts
            lat.append(42.270030)
            lon.append(-71.699885)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#MI' in tweet.text: # Michigan
            lat.append(42.866290)
            lon.append(-84.514843)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#MN' in tweet.text: # Minnesota
            lat.append(45.726258)
            lon.append(-94.483332)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                       
        if '#MS' in tweet.text: # Mississippi
            lat.append(32.829128)
            lon.append(-89.855683)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#MO' in tweet.text: # Missouri
            lat.append(38.735015)
            lon.append(-92.480738)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                       
        if '#MT' in tweet.text: # Montana
            lat.append(47.197600)
            lon.append(-109.662487)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                   
        if '#NE' in tweet.text: # Nebraska
            lat.append(41.242098)
            lon.append(-99.318614)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                       
        if '#NV' in tweet.text: # Nevada
            lat.append(38.903271)
            lon.append(-116.426747)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#NH' in tweet.text: # New Hampshire
            lat.append(43.229182)
            lon.append(-71.576017)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#NJ' in tweet.text: # New Jersey
            lat.append(40.011891)
            lon.append(-74.505838)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#NM' in tweet.text: # New Mexico
            lat.append(34.477320)
            lon.append(-106.164719)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                
        if '#NY' in tweet.text: # New York
            lat.append(40.711634)
            lon.append(-73.936331)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#NC' in tweet.text: # North Carolina
            lat.append(35.777766)
            lon.append(-78.912974)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#ND' in tweet.text: # North Dakota
            lat.append(47.120741)
            lon.append(-100.355791)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
               
        if '#MP' in tweet.text: # Northern Mariana Island's
            lat.append(15.177288)
            lon.append(145.742024)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#OH' in tweet.text: # Ohio
            lat.append(40.140730)
            lon.append(-82.799507)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
              
        if '#OK' in tweet.text: # Oklahoma
            lat.append(35.598095)
            lon.append(-97.402951)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#OR' in tweet.text: # Oregon
            lat.append(43.655112)
            lon.append(-120.709186)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#PA' in tweet.text: # Pennsylvania
            lat.append(40.708446)
            lon.append(-77.797431)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#PR' in tweet.text: # Puerto Rico
            lat.append(18.245539)
            lon.append(-66.476129)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#RI' in tweet.text: # Rhode Island
            lat.append(41.717487)
            lon.append(-71.523872)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#SC' in tweet.text: # South Carolina
            lat.append(34.010105)
            lon.append(-80.540033)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#SD' in tweet.text: # South Dakota
            lat.append(44.418085)
            lon.append(-100.351359)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#TN' in tweet.text: # Tennessee
            lat.append(35.843349)
            lon.append(-86.584571)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#TX' in tweet.text: # Texas
            lat.append(31.211550)
            lon.append(-99.087012)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#UT' in tweet.text: # Utah
            lat.append(39.066880)
            lon.append(-111.276458)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#VT' in tweet.text: # Vermont
            lat.append(44.229969)
            lon.append(-72.741321)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)    

        if '#VA' in tweet.text: # Virginia
            lat.append(37.519345)
            lon.append(-78.230240)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
            
        if '#VI' in tweet.text: # Virgin Islands
            lat.append(17.731312)
            lon.append(-64.762878)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                       
        if '#WA' in tweet.text: # Washington
            lat.append(47.094056)
            lon.append(-120.494907)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                       
        if '#WV' in tweet.text: # West Virginia
            lat.append(38.398489)
            lon.append(-81.000907)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#WI' in tweet.text: # Wisconsin
            lat.append(44.238824)
            lon.append(-89.492394)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                        
        if '#WY' in tweet.text: # Wyoming
            lat.append(43.236438)
            lon.append(-107.514572)
            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#',5))
            _link = tweet.text.find('https://')
            link.append(tweet.text[_link:])
            event_descrip = tweet.text[start:end]
            blank = event_descrip.split('\n')
            filtering = [wn for wn in blank if wn.strip() != ""]
            filtered = ""
            for x in filtering:
                filtered += x
            descrip.append(filtered)
                
#-----------------------------
# Export to csv
#-----------------------------
filename = "usEvents.csv"
cols = ['Lat','Lon','Description','Link','Scale','Size']
nRows = len(lat)
with open(filename,'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    for n_row in range(nRows):
        row = [lat[n_row],lon[n_row],descrip[n_row],link[n_row],2,2]
        csvwriter.writerow(row)
#-----------------------------