import csv

import tweepy

from app.util import geo

# CHANGE WITH YOUR TWITTER API KEYS | it's free apply @ (https://developer.twitter.com/en)
auth = tweepy.OAuthHandler('*YOUR CONSUMER KEY*', '*YOUR SECRET CONSUMER KEY*')
auth.set_access_token('*YOUR ACCESS TOKEN*', '*YOUR SECRET ACCESS TOKEN*')
api = tweepy.API(auth)

# Setting our user source (Defualt: https://twitter.com/IntelPointAlert)
tweets = api.user_timeline(screen_name='IntelPointAlert')

# null lits to store collected data
lat, lon, descrip, link = [], [], [], []

# Looping through each tweet
for tweet in tweets:
    if '#URGENT' in tweet.text:
        hashtags = tweet.entities['hashtags']
        city = hashtags[1]['text']
        try:
            state = hashtags[2]['text']
            location = geo.locate(city, state)
            lat.append(location[0])
            lon.append(location[1])

            start = (tweet.text.find(':') + 2)
            end = (tweet.text.find('#', 5))
            event_descrip = tweet.text[start:end].split('\n')
            descrip.append(event_descrip[0])

            link_start = tweet.text.find('https://')
            link.append(tweet.text[link_start:])

        except IndexError:
            pass

# Export to csv file
filename = "app/data/events/usEvents.csv"
cols = ['Lat', 'Lon', 'Title', 'Link', 'Condition', 'Impact']
nRows = len(lat)
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    for n_row in range(nRows):
        row = [lat[n_row], lon[n_row], descrip[n_row], link[n_row], 2.0, 2.0]
        csvwriter.writerow(row)
