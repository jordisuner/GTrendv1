# import pytrends
from pytrends.request import TrendReq
import requests
import pandas
import lxml

#import BeautifulSoup



gusr = input("Usuari Google:?")
gpwd = input("Pwd Google:?")

GTrendCon = TrendReq(gusr, gpwd, custom_useragent= 'PlayExplore Trends')

#print(GTrendCon.results)

trend_payload = {'q': 'Pizza, Italian, Spaghetti, Breadsticks, Sausage', 'cat': '0-71', 'geo':'ES'}
#trend_payload = {'q': 'colour code, alto voltaje, castle logix, robot turtles, dr. eureka','cat': '8', 'geo':'ES', 'date': 'today 12'}
#https://www.google.com/trends/explore?cat=8&date=today%2012-m&geo=ES&q=colour%20code,alto%20voltaje,castle%20logix,robot%20turtles,dr.%20eureka
# 8->Jocs


# trend
trend = GTrendCon.trend(trend_payload)
print(trend)

# print(gusr)
# print(gpwd)
