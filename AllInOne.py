import requests
import json
import smtplib
import email
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import csv
from SendMail import SendMail

# 获取当日时间	2019-11-10
today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(today_time)

def getWeatherInfo():
    location = 'guangzhou'
    key = '1e9f3d6ab04c484395685a41b3fdbec4'

    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + location + '&key=' + key
    print(url)

    #获取到json数据
    res = requests.get(url)
    #print(type(res))
    #print(res.text)

    #把json数据换成字典形式
    res_dict = json.loads(res.text)
    # print(res_dict)
    # print(res_dict['HeWeather6'])
    # print(res_dict['HeWeather6'][0])
    # print(res_dict['HeWeather6'][0]['basic']) #获取经纬度信息
    location = res_dict['HeWeather6'][0]['basic']

    print(res_dict['HeWeather6'][0]['daily_forecast'])
    result = res_dict['HeWeather6'][0]['daily_forecast']
    city = location['parent_city']+location['location']
    names = ['城市','时间','天气状况','最高温','最低温','日出','日落']
    with open('today_weather.csv', 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(names)
        for data in result:
            date = data['date']
            cond = data['cond_txt_d']
            max = data['tmp_max']
            min = data['tmp_min']
            sr = data['sr']
            ss = data['ss']
            writer.writerows([(city, date, cond, max, min, sr, ss)])
    SendMail()

getWeatherInfo()






