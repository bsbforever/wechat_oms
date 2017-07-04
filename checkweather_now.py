#coding=utf8
import requests
import json
from sendmail_weather import *
def now_weather(now):
    weather={}
    weather['date']=now['date']
    weather['now_day']=now['text_day']
    weather['now_night']=now['text_night']
    weather['now_high']=now['high']
    weather['now_low']=now['low']
    weather['now_scale']=now['wind_scale']
    return weather

def next_weather(nextday):
    weather={}
    weather['date']=nextday['date']
    weather['next_day']=nextday['text_day']
    weather['next_night']=nextday['text_night']
    weather['next_high']=nextday['high']
    weather['next_low']=nextday['low']
    weather['next_scale']=nextday['wind_scale']
    return weather

url='https://api.seniverse.com/v3/weather/daily.json?key=bfaubqmx0hbkdqbb&location=suzhou&language=zh-Hans&unit=c&start=0&days=5'

r = requests.get(url)
content=r.text
content =json.loads(content)
result=content['results']

location=result[0]['location']['name']

now=result[0]['daily'][0]

now_weather=now_weather(now)

#nextday=result[0]['daily'][1]

#next_weather=next_weather(nextday)
mailcontent='今日'+location+'白天天气为'+str(now_weather['now_day'])+',夜晚天气为'+str(now_weather['now_night'])+',最高气温为'+str(now_weather['now_high'])+'度,最低气温'+str(now_weather['now_low'])+'度,风力为'+str(now_weather['now_scale'])+'级'

#print (mailcontent)
send_mail(to_list,'今日天气预报',mailcontent)

