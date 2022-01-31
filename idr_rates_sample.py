import requests


#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.9555731259868e-5,"date":"Sun, 30 Jan 2022 23:55:01 GMT","inverseRate":14376.960487467},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.2440468427552e-5,"date":"Sun, 30 Jan 2022 23:55:01 GMT","inverseRate":16015.254612644}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])