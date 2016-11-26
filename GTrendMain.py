# import pytrends
from pytrends.request import TrendReq
import json
import csv

#import BeautifulSoup



gusr = input("Usuari Google:?")
gpwd = input("Pwd Google:?")

#gusr = '????'
#gpwd = '????'

GTrendCon = TrendReq(gusr, gpwd, custom_useragent= 'PlayExplore Trends')

#print(GTrendCon.results)

#trend_payload = {'q': 'Pizza, Italian, Spaghetti, Breadsticks, Sausage', 'cat': '0-71', 'geo':'ES'}
trend_payload = {'q': 'colour code, alto voltaje, castle logix, robot turtles, dr. eureka','cat': '8', 'geo':'ES', 'date': 'today 12-m'}
#https://www.google.com/trends/explore?cat=8&date=today%2012-m&geo=ES&q=colour%20code,alto%20voltaje,castle%20logix,robot%20turtles,dr.%20eureka
# 8->Jocs


# trend
trend = GTrendCon.trend(trend_payload)
print(trend)


keys = trend.keys()

dResultats = trend['table']

lRResultats = dResultats['rows']
lCResultats = dResultats['cols']


for i in lCResultats:
   #i = {'label': 'Date', 'pattern': '', 'type': 'date', 'id': 'date'}
    print(i['label']+";")

for j in lRResultats:
   #j columnes fila -> {'c': [{'v': '2015-11-29', 'f': 'Nov 28 – Dec 5, 2015'}, {'v': 0.0, 'f': '0'}, {'v': 0.0, 'f': '0'}, {'v': 0.0, 'f': '0'}, {'v': 0.0, 'f': '0'}, {'v': 0.0, 'f': '0'}]}
    z=j['c']
    for y in z:
        print(y['f'] + ";")

f = open('trendresults.txt', 'w')
json.dump(trend,f, indent=4)

