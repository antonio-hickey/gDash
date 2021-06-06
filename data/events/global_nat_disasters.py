"""
Collecting data on natural disasters around the world 

Source:
    - GDAC (Global Disaster Alert & Coordination System)

Targeted output data:
    - [Lat, Lon, Description, Link, Scale, Size]
"""


# Import Modules
from bs4 import BeautifulSoup as bs
import requests as req
import datetime as dt
import pandas as pd
import time
import csv
import os


# URL to Global Disater Alert & Coordination System
URL = "https://www.gdacs.org/xml/rss_24h.xml"
page = req.get(URL) # Request Page
soup = bs(page.content,"lxml") # Parse page as XML

# Null lists for targeted data
titles = []
descrips = []
lats = []
lons = []
scores = []
links = []
texts = []


# Defining data values
event = soup.findAll("item")
for i in event:
    text = i.get_text()
    start = (text.find("https://www.gdacs.org/report.aspx?"))
    links.append(text[start:start+65])
    titles.append(str(i.find("title"))[7:-8]) 
    descrips.append(str(i.find("description"))[13:-14]) 
    lats.append(str(i.find("geo:lat"))[9:-10]) 
    lons.append(str(i.find("geo:long"))[10:-11]) 
    scores.append(str(i.find("gdacs:episodealertscore"))[25:-26])


# Creating columns for dataset
col = ["Lat","Lon","Description","Link","Scale","Size"]


# Creating rows for dataset
rows = []
for ith in range(len(event)):
    _list = [lats[ith],lons[ith],descrips[ith],links[ith],scores[ith],scores[ith]]
    rows.append(_list)


# Render output dataset
filename = 'GND.csv'
with open(filename,'w') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(col)
    for x in rows:
        csvwrite.writerow(x)
