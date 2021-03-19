import requests
import pandas as pd
from bs4 import BeautifulSoup

page=requests.get("https://forecast.weather.gov/MapClick.php?textField1=34.1&textField2=-118.34")  # jis city ka temp scrap krwnana hai uska url dedo
soup=BeautifulSoup(page.content, 'html.parser')
day =soup.find(id="seven-day-forecast-body")
#print(day)
items=day.find_all(class_="forecast-tombstone")
#print(items[0])   # printing fist container only

                    #get_text() ka function tags hata deta hai html css kay
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp temp-high').get_text())
#print(items[0].find(class_='period-name').get_text())

#to get all periods we just have to run a for loop 

periods=[item.find(class_='period-name').get_text() for item in items] # fetching periods
discriptions=[item.find(class_='short-desc').get_text() for item in items]
temps=[item.find(class_='temp').get_text() for item in items]  # temprature ki class upr wali nhi rkengay wrna aik hi ka temp ayga

# print(periods)
# print(discriptions)
# print(temps)

weather_stuff= pd.DataFrame({       # creating table of list using pandas
    "periods":periods,
    "discriptions":discriptions,
    "temps":temps
})

print(weather_stuff)
weather_stuff.to_csv("weather.csv") # creating a csv file of the table