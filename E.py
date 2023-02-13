import bs4
import requests
from selenium import webdriver
import python_weather
import asyncio

url = 'https://www.google.com/search?q=weather&rlz=1C1ONGR_enIN1017IN1017&oq=weather&aqs=chrome.0.69i59j69i57j69i59l2j0i271l2.1285j0j15&sourceid=chrome&ie=UTF-8'


async def get_weather(city):
    list =[]
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get(city)
  
    # returns the current day's forecast temperature (int)
    # return weather.current.temperature
    list.append(weather.current.temperature)
  
    #get the weather forecast for a few days
    for forecast in weather.forecasts:
        list.extend([forecast.date, forecast.astronomy])
  
      # hourly forecasts
    for hourly in forecast.hourly:
        list.append(f' --> {hourly!r}')
        
    return list

h = asyncio.run(get_weather("kerala"))
print(type(h))

'''wd = webdriver.Chrome('D://chromedriver.exe')
r = requests.get(url)
page = r.text

soup = bs4.BeautifulSoup(page,'html.parser')

print(soup.prettify())'''
