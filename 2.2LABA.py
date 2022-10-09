import requests

city = "Almata,KZ"
key = "63dbe6b06816bd07ba7b4f0c55978d85"


qq = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
data = qq.json()

for i in data['list']:
    print('дата:', i['dt_txt'],
          '\r\nТемпереатура:', '{0:+3.0f}'.format(i['main']['temp']),
          '\r\nСкорость ветра:', i['wind']['speed'],
          '\r\nВидимость:', i['visibility'])