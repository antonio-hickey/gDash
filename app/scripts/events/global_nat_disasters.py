"""
Collecting data on natural disasters around the world

Source:
    - GDAC (Global Disaster Alert & Coordination System)

Targeted output data:
    - [Lat, Lon, Title, Link, Condition, Impact]
 """
import csv

import requests as req
from bs4 import BeautifulSoup as bs

from app.util.links import GDACS

URL = GDACS
page = req.get(URL)
soup = bs(page.content, "lxml")


titles = []
descrips = []
lats = []
lons = []
scores = []
links = []

event = soup.findAll("item")
for i in event:
    text = i.get_text()
    start = (text.find("https://www.gdacs.org/report.aspx?"))
    links.append(text[start:start+62])
    titles.append(str(i.find("title"))[7:-8])
    descrip = (str(i.find("description"))[13:-14])
    lats.append(str(i.find("geo:lat"))[9:-10])
    lons.append(str(i.find("geo:long"))[10:-11])
    score = str(i.find("gdacs:episodealertscore"))[25:-26]
    if score == "1":
        scores.append(3)
    if score == "3":
        scores.append(1)
    if score == "2":
        scores.append(2)

    if "Volcano" in descrip:
        start = descrip.find("Volcano")
        end = descrip.find(".")
        filter_out = "according to the regional VAAC"
        descrips.append(descrip[start:(end-len(filter_out))])

    if "earthquake" in descrip:
        magn_start = (descrip.find("Magnitude"))
        magn = descrip[magn_start:]
        magn_end = (magn.find(","))
        magnitude = (magn[:magn_end])
        filter2 = (magnitude.find(" ")+1)
        magnitude = magn[filter2:magn_end]
        magnitude = ''.join(('(', magnitude, ')'))
        start = (descrip.find(",")+5)
        end = (descrip.find("."))
        title_pre = descrip[start:end]
        ignore = title_pre.find("potentially")
        title = title_pre[:ignore]
        descrips.append(''.join((title, magnitude)))

    if "forest fire" in descrip:
        start = descrip.find("forest")
        end = descrip[start:].find(",")
        descrips.append(descrip[start:end+start])

    if "Tropical" in descrip:
        trop_start = (descrip.find("Tropical"))
        trop_pre = descrip[trop_start:]
        speed_start = trop_pre.find("speed of")
        speed_pre = trop_pre[speed_start+len("speed of"):]
        speed_end = speed_pre.find(')')
        speed = (speed_pre[:speed_end])
        speed = ''.join(('(', speed, ')'))
        descrips.append(''.join(("Tropical Storm", speed)))

    if "Drought" in descrip:
        drought_start = descrip.find("Drought")
        descrips.append(descrip[drought_start:])

    if "Hurricane" in descrip:
        type_ = "Hurricane/Typhoon "
        type_start = descrip.find(type_)
        _base = (descrip[type_start:])
        test = _base.find(';')+8
        speed = ''.join(('(', _base[test-6:test], ')'))
        descrips.append(''.join((type_, speed)))


col = ["Lat", "Lon", "Title", "Link", "Condition", "Impact"]

rows = []
for ith in range(len(event)):
    _list = [lats[ith], lons[ith], descrips[ith], links[ith], scores[ith], scores[ith]]
    rows.append(_list)

filename = 'app/data/events/GND.csv'
with open(filename, 'w') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(col)
    for x in rows:
        csvwrite.writerow(x)
