import requests

city = "Almata,KZ"
key = "63dbe6b06816bd07ba7b4f0c55978d85"


qq = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
data = qq.json()

print('Лучший город:',data['name'])
print('сейчас:',data['main']['temp'])
print('Скорость ветра:',data['wind']['speed'])
print('Видимость:',data['visibility'])
