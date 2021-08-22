"""
Collecting data on conflict worldwide

Source:
    - Council on Foriegn Relations

Targeted output data:
    - [Lat, Lon, Title, Link, Condition, Impact]

"""

# Import Modules
import requests as req
import json
import csv


URL = "https://microsites-live-backend.cfr.org/conflict/map/json"
page = req.get(URL)
response = json.loads(page.content)
data = response['features']
rows = []
for dp in data:
    cords = (dp['geometry']['coordinates'])
    lat = (cords[1])
    lon = (cords[0])
    title = (dp['properties']['title'])
    link = ('https://www.cfr.org' + dp['properties']['link'])
    impact = (dp['properties']['severity']['us']['value'])
    condition = (dp['properties']['severity']['usConflictStatus']['value'])

    if impact == 'critical':
        impact = '1'
    elif impact == 'significant':
        impact = '2'
    elif impact == 'limited':
        impact = '3'
    
    if condition == 'worsening':
        condition = '3'
    elif condition == 'unchanging':
        condition = '2'
    elif condition == 'improving':
        condition = '1'

    rows.append([lat, lon, title, link, condition, impact])

filename = "geoConflicts.csv"
cols = ['Lat', 'Lon', 'Title', 'Link', 'Condition', 'Impact']
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    for row in rows:
        csvwriter.writerow(row)

